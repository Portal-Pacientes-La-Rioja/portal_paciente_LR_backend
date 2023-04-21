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
    direction = address[1]
    location = geo.geocode(direction)
    if location is not None:
        lat = location.latitude if location.latitude is not None else 0
        long = location.longitude if location.longitude is not None else 0
        cursor.execute('UPDATE institutions SET `lat`=%s, `long`=%s WHERE id=%s', (lat, long, institution_id))
        conn.commit()
    else:
        print('No se pudo obtener la latitud y longitud para el establecimiento con ID', institution_id)

conn.close()
