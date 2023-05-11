# README - Script Geocode Users
Este script se encarga de cargar los datos de latitud y longitud en cada uno de los usuarios registrados en la base de datos.

## Requerimientos
Para ejecutar el script se requiere tener instaladas las siguientes bibliotecas de Python:
+ PyMySQL.
+ Geopy.

Las cuales pueden ser instaladas con el siguiente comando:

`pip install -r requirements.txt`

## Variables de entorno
Antes de ejecutar el script, se deben configurar las siguientes variables de entorno:

| Variable de Entorno | Descripción                                            |
| ------------------- |--------------------------------------------------------|
| DB_HOST             | dirección IP o nombre de dominio del servidor de la BD |
| DB_USER             | nombre de usuario de la BD                             |
| DB_PASSWORD         | contraseña de la BD                                    |
| DB_NAME             | nombre de la BD                                        |

## Uso
Ejecutar el script desde la línea de comandos de Python.

`python geocode_users.py`

El script se encargará de cargar los datos de latitud y longitud en la tabla person.
