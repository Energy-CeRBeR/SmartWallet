from pydantic import BaseModel


class TypeCreate(BaseModel):
    name: str


class CardCreate(BaseModel):
    name: str
    type_id: int
    user_id: int
    balance: int
