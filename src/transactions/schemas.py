from pydantic import BaseModel


class CreateInCategory(BaseModel):
    name: str


class CreateExCategory(BaseModel):
    name: str


class CreateIncome(BaseModel):
    category_id: int
    card_id: int
    amount: int
    description: str


class CreateExpense(BaseModel):
    category_id: int
    card_id: int
    amount: int
    description: str


class UpdateIncome(BaseModel):
    id: int
    category_id: int
    card_id: int
    amount: int
    description: str


class UpdateExpense(BaseModel):
    id: int
    category_id: int
    card_id: int
    amount: int
    description: str
