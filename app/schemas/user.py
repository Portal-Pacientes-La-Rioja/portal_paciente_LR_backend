from typing import Optional, List
from pydantic import BaseModel


class User(BaseModel):
    # id: Optional[int]
    username: Optional[str]
    # password: Optional[str]
    id_person: Optional[int]
    id_user_status: Optional[int]


class UserAdmin(User):
    id: Optional[int]
    is_admin_activate: Optional[int]
    pass

    class Config:
        orm_mode = True
