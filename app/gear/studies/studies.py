import os

from fastapi import File, UploadFile
from sqlalchemy.orm import Session

from app.gear.studies.config import UPLOAD_DIR

from app.models.person import Person as model_person
from app.schemas.responses import ResponseNOK, ResponseOK


class StudiesController:
    def __init__(self, db: Session):
        self.db = db

    async def upload_study(self, person_id: int, study: UploadFile = File(...)):
        # Validating if the person exists
        existing_person = (
            self.db.query(model_person).where(model_person.id == person_id).first()
        )

        if existing_person is None:
            return ResponseNOK(message=f"Non existent person_id: {str(person_id)}", code=417)

        try:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            file_path = os.path.join(UPLOAD_DIR, study.filename)
            with open(file_path, "wb") as file:
                file.write(await study.read())

            return ResponseOK(message="Study loaded successfully", code=201)

        except Exception as e:
            return ResponseNOK(message=f"Error: {str(e)}", code=500)

