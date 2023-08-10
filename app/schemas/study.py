from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Studies(BaseModel):
    study_id: Optional[int]
    study_name: Optional[str]
    description: Optional[str]
    upload_date: Optional[datetime]
