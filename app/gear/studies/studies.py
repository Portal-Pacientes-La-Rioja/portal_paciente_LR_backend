import os

from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.gear.studies.config import UPLOAD_DIR

from app.models.person import Person as model_person
from app.schemas.responses import ResponseNOK


class StudiesController:
    def __init__(self, db: Session):
        self.db = db

    async def upload_study(self, person_id: int, study: UploadFile = File(...)):
        existing_person = (
            self.db.query(model_person).where(model_person.id == person_id).first()
        )

        if existing_person is None:
            return ResponseNOK(message=f"Non existent person_id: {str(person_id)}", code=417)

        try:
            person_dir = os.path.join(UPLOAD_DIR, str(person_id))
            os.makedirs(person_dir, exist_ok=True)

            file_path = os.path.join(person_dir, study.filename)
            with open(file_path, "wb") as file:
                file.write(await study.read())

            return JSONResponse({"message": "Estudio cargado exitosamente"})

        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)
