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
cursor.execute('SELECT id, address_street, address_number, department, locality FROM person')
addresses = cursor.fetchall()

geo = Nominatim(user_agent="portal-paciente-lr")

for address in addresses:
    person_id = address[0]
    direction = f"{address[1]} {address[2]}, {address[3]}, {address[4]}"
    location = geo.geocode(direction)
    if location is not None:
        lat = location.latitude
        long = location.longitude
        cursor.execute('UPDATE person SET `lat`=%s, `long`=%s WHERE id=%s', (lat, long, person_id))
        conn.commit()
    else:
        print('No se pudo obtener la latitud y longitud para la persona con ID', person_id)

conn.close()
