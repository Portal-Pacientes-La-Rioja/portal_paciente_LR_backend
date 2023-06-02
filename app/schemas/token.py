from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    is_admin: int
    is_superadmin: int
