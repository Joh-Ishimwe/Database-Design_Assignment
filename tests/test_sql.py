import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database.sql_db import SessionLocal
from sqlalchemy.sql import text

db = SessionLocal()

try:
    db.execute(text("SELECT 1"))  
    print("Connected to PostgreSQL successfully!")
except Exception as e:
    print("Failed to connect:", e)
finally:
    db.close()