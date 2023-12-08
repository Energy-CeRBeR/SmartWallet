from pydantic import BaseModel


class TypeCreate(BaseModel):
    id: int
    name: str


class CardCreate(BaseModel):
    id: int
    name: str
    type_id: int
    user_id: int
    balance: int
    incomes: dict
    expenses: dict
