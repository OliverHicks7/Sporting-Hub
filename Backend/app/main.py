from fastapi import FastAPI
from app.database import engine
from sqlalchemy import text
from app import models
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db
from app.models import User

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            return {"db": "connected", "result": result.scalar()}
    except Exception as e:
        return {"db": "failed", "error": str(e)}
    
@app.post("/users")
def create_user(username: str, favourite_sport: str, db: Session = Depends(get_db)):
    user = User(username=username, favourite_sport=favourite_sport)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user