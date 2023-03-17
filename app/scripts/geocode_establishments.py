from app.config.database import SessionLocal
from app.models.establishment import Establishment
from geopy.geocoders import Nominatim

db = SessionLocal()

addresses = db.query(Establishment.id, Establishment.address).all()

geo = Nominatim(user_agent="portal-paciente-lr")

for address in addresses:
    establishment_id = address[0]
    direction = address[1]
    location = geo.geocode(direction)
    if location is not None:
        lat = location.latitude
        long = location.longitude
        db.query(Establishment).filter_by(id=establishment_id).update(latitud=lat, longitude=long)
        db.commit()
    else:
        print('No se pudo obtener la latitud y longitud para el establecimiento con ID:', establishment_id)
