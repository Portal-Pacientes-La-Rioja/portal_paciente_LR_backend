import googlemaps
from app.config.config import GOOGLE_MAPS_API_KEY

from sqlalchemy.orm import Session
from sqlalchemy.exc import PendingRollbackError

from app.gear.log.main_logger import MainLogger, logging

from app.models.person import Person as model_person
from app.models.institutions import Institutions as model_institution


class ShortestRoute:
    log = MainLogger()
    module = logging.getLogger(__name__)

    def __init__(self, db: Session):
        self.db = db

    def calculate_shortest_route(self, person_id: int, institution_id: int):
        gmaps = googlemaps.Client(key=f"{GOOGLE_MAPS_API_KEY}")

        directions_result = gmaps.directions(
            self.get_person_location(person_id), self.get_institution_location(institution_id), mode="driving"
        )

        if len(directions_result) > 0:
            shortest_route = directions_result[0]

            waypoints = []
            for step in shortest_route["legs"][0]["steps"]:
                spot = step["start_location"]
                waypoints.append((spot["lat"], spot["lng"]))
            final_spot = shortest_route["legs"][0]["end_location"]
            waypoints.append((final_spot["lat"], final_spot["lng"]))

            return waypoints
        else:
            return None

    def get_person_location(self, person_id: int):
        try:
            person = (
                self.db.query(model_person.lat, model_person.long).filter(model_person.id == person_id).first()
            )
            if person:
                return person.lat, person.long
            else:
                return None, None
        except PendingRollbackError as e:
            self.log.log_error_message(str(e) + " [" + str(person_id) + "]", self.module)
            self.db.rollback()
            return None, None
        except Exception as e:
            self.log.log_error_message(e, self.module)
            return None, None

    def get_institution_location(self, institution_id: int):
        try:
            institution = (
                self.db.query(model_institution.lat, model_institution.long)
                    .filter(model_institution.id == institution_id)
                    .first()
            )
            if institution:
                return institution.lat, institution.long
            else:
                return None, None
        except PendingRollbackError as e:
            self.log.log_error_message(str(e) + " [" + str(institution_id) + "]", self.module)
            self.db.rollback()
            return None, None
        except Exception as e:
            self.log.log_error_message(e, self.module)
            return None, None
