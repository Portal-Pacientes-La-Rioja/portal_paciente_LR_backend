from geopy.geocoders import Nominatim


class Geolocation:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="portal-paciente")

    def get_lat_long_from_address(self, address: str):
        location = self.geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude

        return None
