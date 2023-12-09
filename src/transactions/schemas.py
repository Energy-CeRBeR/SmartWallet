from pydantic import BaseModel


class CreateInCategory(BaseModel):
    id: int
    name: str
    user_id: int


class CreateExCategory(BaseModel):
    id: int
    name: str
    user_id: int


class CreateIncome(BaseModel):
    id: int
    category_id: int
    card_id: int
    amount: int
    description: str


class CreateExpense(BaseModel):
    id: int
    category_id: int
    card_id: int
    amount: int
    description: str
