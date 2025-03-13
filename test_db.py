from database import SessionLocal
from sqlalchemy.sql import text

db = SessionLocal()

try:
    db.execute(text("SELECT 1"))  
    print("Connected to Render PostgreSQL successfully!")
except Exception as e:
    print("Failed to connect:", e)
finally:
    db.close()
