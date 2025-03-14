from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use the Render PostgreSQL URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Database Engine with SSL
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "sslmode": "require",  # Enable SSL
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()