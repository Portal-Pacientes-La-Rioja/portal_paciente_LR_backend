import googlemaps
import polyline

from app.config.config import GOOGLE_MAPS_API_KEY
from typing import Tuple

from sqlalchemy.orm import Session
from sqlalchemy.exc import PendingRollbackError

from app.gear.log.main_logger import MainLogger, logging

from app.models.person import Person as model_person
from app.models.institutions import Institutions as model_institution


class ErrorDirecctionCalculation(Exception):
    pass


class ShortestRoute:
    log = MainLogger()
    module = logging.getLogger(__name__)

    def __init__(self, db: Session):
        self.db = db

    def calculate_shortest_route(self, person_id: int, institution_id: int):
        gmaps = googlemaps.Client(key=f"{GOOGLE_MAPS_API_KEY}")

        person_location, institution_location = self.get_start_end_point(person_id, institution_id)

        try:
            directions_result = gmaps.directions(person_location, institution_location)  # mode=driving by default.
        except TypeError:
            # This can be occur if directions() receive some None data input
            raise ErrorDirecctionCalculation

        if directions_result:
            polygon = directions_result[0]["overview_polyline"]["points"]
            return polyline.decode(polygon)
        else:
            raise ErrorDirecctionCalculation

    def get_start_end_point(self, person_id: int, institution_id: int) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        try:
            person_location = self.get_person_location(person_id)
            institution_location = self.get_institution_location(institution_id)
        except PendingRollbackError as e:
            self.log.log_error_message(str(e) + " [" + str(person_id) + "]", self.module)
            self.db.rollback()
            raise ErrorDirecctionCalculation
        except Exception as e:
            self.log.log_error_message(e, self.module)
            raise ErrorDirecctionCalculation
        return person_location, institution_location

    def get_person_location(self, person_id: int):
        person = (
            self.db.query(model_person.lat, model_person.long).filter(model_person.id == person_id).first()
        )
        return person.lat, person.long

    def get_institution_location(self, institution_id: int):
        institution = (
            self.db.query(model_institution.lat, model_institution.long)
                .filter(model_institution.id == institution_id)
                .first()
        )
        return institution.lat, institution.long
