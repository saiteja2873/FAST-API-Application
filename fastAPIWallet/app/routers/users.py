from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("", response_model=List[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    result = []
    for u in users:
        balance = u.wallet.balance if u.wallet else 0.0
        result.append(
            schemas.UserOut(id=u.id, name=u.name, email=u.email, phone=u.phone, balance=balance)
        )
    return result
