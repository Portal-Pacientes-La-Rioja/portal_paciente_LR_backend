import base64
import io
import os
from datetime import datetime

import filetype

from fastapi import File, UploadFile
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.gear.log.main_logger import MainLogger, logging
from app.gear.studies.config import UPLOAD_DIR

from app.models.person import Person as model_person
from app.models.study import Studies as model_studies
from app.models.study_type import StudyType as model_study_type
from app.schemas.responses import ResponseNOK, ResponseOK
from app.schemas.returned_object import ReturnMessage

ALLOWED_EXTENSIONS = ["pdf", "jpeg", "jpg", "png"]
MAX_FILE_SIZE_MB = 10


class StudiesController:
    log = MainLogger()
    module = logging.getLogger(__name__)

    def __init__(self, db: Session):
        self.db = db

    async def upload_study(
        self,
        person_id: int,
        description: str,
        study_type_id: int,
        study: UploadFile = File(...),
    ):
        # Validating if the person exists
        existing_person = (
            self.db.query(model_person).where(model_person.id == person_id).first()
        )

        if existing_person is None:
            return ResponseNOK(
                message=f"Non existent person_id: {str(person_id)}", code=417
            )

        # Validating the file type
        # TODO: esto es un binario, por lo que creo que el file_extension
        #  del filename puede no ser el correcto, depende de cómo lo envía frontend,
        #  o de cómo lo sube el usuario. Lo comento para no bloquear al frontend, pero
        #  deberíamos reveerlo.
        # file_extension = study.filename.split('.')[-1].lower()
        # if file_extension not in ALLOWED_EXTENSIONS:
        #     return ResponseNOK(message="Invalid file type", code=400)

        # Validating the MIMETYPE
        mime_type = filetype.guess(study.file.read())
        study.file.seek(0)
        if mime_type is None or mime_type.mime.split("/")[-1] not in ALLOWED_EXTENSIONS:
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

            timestamp = datetime.now().strftime('%Y%m%d%H%M')
            file_extension = study.filename.split('.')[-1].lower()
            file_name_without_extension = os.path.splitext(os.path.basename(study.filename))[0]
            new_file_name = f"{file_name_without_extension}_{timestamp}.{file_extension}"

            file_path = os.path.join(UPLOAD_DIR, new_file_name)
            file_content = open(file_path, "wb+")
            file_content.write(await study.read())
            file_content.close()
            with open(file_path, "rb") as bin_file:
                b64_string_file = base64.b64encode(bin_file.read())

            new_study = model_studies(
                id_person=person_id,
                id_study_type=study_type_id,
                study_name=new_file_name,
                description=description,
                file_path=b64_string_file,
            )

            self.db.add(new_study)
            self.db.commit()

            return ResponseOK(message="Study loaded successfully", code=201)

        except Exception as e:
            self.db.rollback()
            return ResponseNOK(message=f"Error: {str(e)}", code=500)

    def get_study_types(self):
        try:
            result = []
            study_types = self.db.query(model_study_type).all()

            for u in study_types:
                result.append({"id": u.id, "type_name": u.type_name})

            return result
        except Exception as e:
            self.log.log_error_message(e, self.module)
            return ResponseNOK(message=f"Error: {str(e)}", code=417)

    def get_studies_for_person(self, person_id: int):
        # Validating person_id
        if person_id is None:
            return ResponseNOK(message="Person ID is required", code=400)

        try:
            result = []
            studies_list = (
                self.db.query(model_studies)
                .where(model_studies.id_person == person_id)
                .all()
            )

            # No studies found for the specified person
            if not studies_list:
                return result

            for u in studies_list:
                result.append(
                    {
                        "study_id": u.id,
                        "study_name": u.study_name,
                        "description": u.description,
                        "upload_date": u.upload_date,
                    }
                )

            return result
        except Exception as e:
            self.log.log_error_message(e, self.module)
            return ResponseNOK(message=f"Error: {str(e)}", code=417)

    def get_study_by_id(self, study_id: int):
        try:
            study = (
                self.db.query(model_studies).where(model_studies.id == study_id).first()
            )

            if study is None:
                return ResponseNOK(
                    message=f"Study with ID {study_id} not found", code=404
                )

            decoded_file = base64.b64decode(study.file_path)
            file_stream = io.BytesIO(decoded_file)

            return StreamingResponse(
                file_stream,
                headers={
                    "Content-Disposition": f"attachment; filename={study.study_name}"
                },
            )
        except Exception as e:
            self.log.log_error_message(e, self.module)
            return ResponseNOK(message=f"Error: {str(e)}", code=417)

    def get_studies_by_type(self, study_type_id: int):
        try:
            result = []
            studies_list = (
                self.db.query(model_studies)
                .where(model_studies.id_study_type == study_type_id)
                .all()
            )

            # No studies found for the specified type
            if not studies_list:
                return result

            for u in studies_list:
                result.append(
                    {
                        "study_id": u.id,
                        "study_name": u.study_name,
                        "description": u.description,
                        "upload_date": u.upload_date,
                    }
                )

            return result
        except Exception as e:
            self.log.log_error_message(e, self.module)
            return ResponseNOK(message=f"Error: {str(e)}", code=417)

    def delete_study(self, study_id: int):
        try:
            # Validating if the study exists
            existing_study = self.db.query(model_studies).get(study_id)

            if existing_study is None:
                return ReturnMessage(message="Nonexistent study.", code=417)

            # Removing file from directory
            file_path = os.path.join(UPLOAD_DIR, existing_study.study_name)
            if os.path.exists(file_path):
                os.remove(file_path)

            # Removing file from database
            self.db.delete(existing_study)
            self.db.commit()

            return ReturnMessage(message="Study deleted successfully.", code=201)

        except Exception as e:
            self.db.rollback()
            self.log.log_error_message(e, self.module)
            return ReturnMessage(message="Study cannot be deleted.", code=417)
