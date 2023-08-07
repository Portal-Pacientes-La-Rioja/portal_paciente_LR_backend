import base64
import os
import filetype

from fastapi import File, UploadFile
from sqlalchemy.orm import Session

from app.gear.studies.config import UPLOAD_DIR

from app.models.person import Person as model_person
from app.models.study import Studies as model_studies
from app.schemas.responses import ResponseNOK, ResponseOK

ALLOWED_EXTENSIONS = ['pdf', 'jpeg', 'jpg', 'png']
MAX_FILE_SIZE_MB = 10


class StudiesController:
    def __init__(self, db: Session):
        self.db = db

    async def upload_study(self, person_id: int, description: str, study_type_id: int, study: UploadFile = File(...)):
        # Validating if the person exists
        existing_person = (
            self.db.query(model_person).where(model_person.id == person_id).first()
        )

        if existing_person is None:
            return ResponseNOK(message=f"Non existent person_id: {str(person_id)}", code=417)

        # Validating the file type
        file_extension = study.filename.split('.')[-1].lower()
        if file_extension not in ALLOWED_EXTENSIONS:
            return ResponseNOK(message="Invalid file type", code=400)

        # Validating the MIMETYPE
        mime_type = filetype.guess(study.file.read())
        study.file.seek(0)
        if mime_type is None or mime_type.mime.split('/')[-1] not in ALLOWED_EXTENSIONS:
            return ResponseNOK(message="Invalid MIMETYPE", code=400)

        # Validating the file size
        file_size_mb = study.file.seek(0, os.SEEK_END) / (1024 * 1024)
        study.file.seek(0)
        if file_size_mb > MAX_FILE_SIZE_MB:
            return ResponseNOK(message="File size too large", code=413)

        # Validating duplicates
        existing_study = (
            self.db.query(model_studies)
            .where(model_studies.id_person == person_id)
            .where(model_studies.study_name == study.filename)
            .first()
        )
        if existing_study:
            return ResponseNOK(message="Duplicated file for this person", code=409)

        try:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            file_path = os.path.join(UPLOAD_DIR, study.filename)
            file_content = open(file_path, "wb+")
            file_content.write(await study.read())
            file_content.close()
            with open(file_path, "rb") as bin_file:
                b64_string_file = base64.b64encode(bin_file.read())

            new_study = model_studies(
                id_person=person_id,
                id_study_type=study_type_id,
                study_name=study.filename,
                description=description,
                file_path=b64_string_file,
            )

            self.db.add(new_study)
            self.db.commit()

            return ResponseOK(message="Study loaded successfully", code=201)

        except Exception as e:
            self.db.rollback()
            return ResponseNOK(message=f"Error: {str(e)}", code=500)
