from typing import Optional, List, Union

from pydantic import BaseModel
from .institutions import Institution




class User(BaseModel):
    # id: Optional[int]
    username: Optional[str]
    # password: Optional[str]
    id_person: Optional[int]
    id_user_status: Optional[int]



class UserAdmin(User):
    id: Optional[int]
    is_admin_activate: Optional[int]
    institutions:  Optional[list]
    old_institutions: Optional[list]

    class Config:
        orm_mode = True


class CreateUserAdmin(BaseModel):
    username: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True
