from fastapi_mail import MessageSchema
from sqlalchemy.orm import Session

from app.config.config import (
    MAIL_USERNAME,
)
from app.gear.log.main_logger import MainLogger, logging
from app.gear.mailer.mailer import send_email
from app.main import get_db
from app.models.person import Person
from app.models.institutions import Institutions


db: Session = next(get_db())

log = MainLogger()
module = logging.getLogger(__name__)


async def send_turno_mail(person_id: str, subject: str, body: str) -> bool:
    try:
        existing_person: Person = (
            db.query(Person).where(Person.id == person_id).first()
        )
    except Exception as e:
        log.log_error_message("Error querying Person object: " + str(e), module)
        db.rollback()
        return False

    institution: Institutions = (
        db.query(Institutions).where(Institutions.id == existing_person.id_usual_institution).first()
    )

    email_institution = [institution.email] if institution.email else []

    message = MessageSchema(
        subject=subject,
        recipients=[MAIL_USERNAME] + email_institution,
        body=body,
        # subtype="html",
    )

    # TODO: Almacenar person_id + subject (y un status? o fecha?) en la base de datos,
    #  después vemos que se puede hacer

    try:
        await send_email(message)
    except Exception as e:
        log.log_error_message("Error sending email: " + str(e), module)
        return False
    log.log_info_message("Email sent successfully.", module)
    return True
