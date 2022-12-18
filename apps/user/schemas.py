from pydantic import BaseModel


class UserIn(BaseModel):
    first_name: str
    last_name: str
    password: str


class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
