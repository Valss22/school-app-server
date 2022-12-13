from pydantic import BaseModel


class UserIn(BaseModel):
    firstname: str
    lastname: str
    password: str
