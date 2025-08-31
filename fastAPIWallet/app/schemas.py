from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional, Literal, List
from datetime import datetime

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    balance: float
    class Config:
        from_attributes = True

class WalletUpdateIn(BaseModel):
    user_id: int
    amount: float = Field(..., gt=0)
    action: Literal["credit", "debit"]
    note: Optional[str] = None
    @field_validator("action")
    def lower_action(cls, v): return v.lower()


class WalletUpdateOut(BaseModel):
    user_id: int
    new_balance: float
    last_transaction_id: int

class TransactionOut(BaseModel):
    id: int
    user_id: int
    amount: float
    action: Literal["credit", "debit"]
    note: Optional[str]
    created_at: datetime
    class Config:
        from_attributes = True
