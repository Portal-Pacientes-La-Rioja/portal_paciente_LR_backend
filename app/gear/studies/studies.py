import os

from fastapi import File, UploadFile
from sqlalchemy.orm import Session

from app.gear.studies.config import UPLOAD_DIR

from app.schemas.responses import ResponseNOK, ResponseOK


class StudiesController:
    def __init__(self, db: Session):
        self.db = db

    async def upload_study(self, study: UploadFile = File(...)):
        try:
            os.makedirs(UPLOAD_DIR, exist_ok=True)

            file_path = os.path.join(UPLOAD_DIR, study.filename)
            with open(file_path, "wb") as file:
                file.write(await study.read())

            return ResponseOK(message="Study loaded successfully", code=201)

        except Exception as e:
            return ResponseNOK(message=f"Error: {str(e)}", code=500)

