from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/{user_id}", response_model=List[schemas.TransactionOut])
def get_transactions(user_id: int, db: Session = Depends(get_db)):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.user_id == user_id)
        .order_by(models.Transaction.created_at.desc())
        .all()
    )
