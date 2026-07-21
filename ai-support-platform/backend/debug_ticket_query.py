from app.database.engine import SessionLocal, engine
from sqlalchemy import text

print(f"Engine: {engine.url}")

db = SessionLocal()
print("Session created")

print("Testing SELECT 1")

result = db.execute(text("SELECT 1"))

print("SELECT 1 returned:", result.scalar())

db.close()
