from fastapi import FastAPI
from app.database import engine
from sqlalchemy import text

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