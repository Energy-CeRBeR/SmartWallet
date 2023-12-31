from pydantic import BaseModel


class CardCreate(BaseModel):
    name: str
    type_id: int
    balance: int


class CardUpdate(BaseModel):
    id: int
    name: str
    type_id: int
    balance: float

