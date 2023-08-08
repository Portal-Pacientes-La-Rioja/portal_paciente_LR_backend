from typing import Optional
from pydantic import BaseModel


class StudyType(BaseModel):
    id: Optional[int]
    type_name: Optional[str]
