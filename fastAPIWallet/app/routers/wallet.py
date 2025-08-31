from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/wallet", tags=["Wallet"])

@router.post("/update", response_model=schemas.WalletUpdateOut)
def update_wallet(payload: schemas.WalletUpdateIn, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == payload.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not user.wallet:
        user.wallet = models.Wallet(balance=0.0)
        db.add(user.wallet)
        db.flush()

    if payload.action == "debit" and user.wallet.balance < payload.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    delta = payload.amount if payload.action == "credit" else -payload.amount
    user.wallet.balance += delta

    tx = models.Transaction(user_id=user.id, amount=payload.amount, action=payload.action, note=payload.note)
    db.add(tx)
    db.flush()

    db.commit()
    db.refresh(user.wallet)

    return schemas.WalletUpdateOut(user_id=user.id, new_balance=user.wallet.balance, last_transaction_id=tx.id)
