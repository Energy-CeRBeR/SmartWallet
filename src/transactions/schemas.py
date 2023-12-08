from pydantic import BaseModel


class CreateInCategory(BaseModel):
    id: int
    name: str
    user_id: int


class CreateExCategory(BaseModel):
    id: int
    name: str
    user_id: int
