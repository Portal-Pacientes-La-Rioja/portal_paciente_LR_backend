import os

import pymysql
from geopy.geocoders import Nominatim

conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    db=os.getenv("DB_NAME")
)

cursor = conn.cursor()
cursor.execute('SELECT id, domicilio FROM institutions')
addresses = cursor.fetchall()

geo = Nominatim(user_agent="portal-paciente-lr")

for address in addresses:
    institution_id = address[0]
    direction = address[1] + ", La Rioja, Argentina"
    location = geo.geocode(direction, timeout=15)
    if location is not None:
        lat = location.latitude
        long = location.longitude
        cursor.execute('UPDATE institutions SET `lat`=%s, `long`=%s WHERE id=%s', (lat, long, institution_id))
        conn.commit()
    else:
        print(f'No se pudo obtener la latitud y longitud para el establecimiento con ID {institution_id}, direccion: {direction}')

conn.close()
