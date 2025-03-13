from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use the Render PostgreSQL URL
DATABASE_URL = "postgresql://laptopdb_user:RgRtnEoW5FdENLIAu7ABvzIutmxpacBu@dpg-cv8balbqf0us73b6eg40-a.oregon-postgres.render.com/laptopdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
