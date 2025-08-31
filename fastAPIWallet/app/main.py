from fastapi import FastAPI
from sqlalchemy.orm import Session
from .database import engine, Base, SessionLocal
from .routers import users, wallet, transactions
from . import models
import os

app = FastAPI(title="Wallet Service", version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(wallet.router)
app.include_router(transactions.router)

@app.on_event("startup")
def seed():
    if os.getenv("SEED_ON_STARTUP", "true").lower() != "true":
        return
    db: Session = SessionLocal()
    if not db.query(models.User).first():
        demo = [
            models.User(name="Alice", email="alice@example.com", phone="1111111111"),
            models.User(name="Bob", email="bob@example.com", phone="2222222222"),
        ]
        db.add_all(demo)
        db.flush()
        for u in demo:
            db.add(models.Wallet(user_id=u.id, balance=0.0))
        db.commit()
    db.close()

@app.get("/")
def root():
    return {"status": "ok", "docs": "/docs"}
