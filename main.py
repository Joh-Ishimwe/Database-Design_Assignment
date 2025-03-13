from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import engine, SessionLocal
import models
from models import Laptop, PriceHistory
from pydantic import BaseModel
# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Dependency: Get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for request validation
class LaptopCreate(BaseModel):
    Company: str
    Product: str
    TypeName: str
    Inches: float
    Weight: float
    Price_euros: float
    OS: str
    ScreenID: int
    CPU_ID: int
    GPU_ID: int
    StorageID: int

# ---------------- CRUD Operations ----------------

# Create a new laptop (POST)
@app.post("/laptops/")
def create_laptop(laptop: LaptopCreate, db: Session = Depends(get_db)):
    new_laptop = Laptop(**laptop.dict())
    db.add(new_laptop)
    db.commit()
    db.refresh(new_laptop)
    return new_laptop

# Read all laptops (GET)
@app.get("/laptops/")
def get_laptops(db: Session = Depends(get_db)):
    return db.query(Laptop).all()

# Read a single laptop by ID (GET)
@app.get("/laptops/{laptop_id}")
def get_laptop(laptop_id: int, db: Session = Depends(get_db)):
    laptop = db.query(Laptop).filter(Laptop.LaptopID == laptop_id).first()
    if not laptop:
        raise HTTPException(status_code=404, detail="Laptop not found")
    return laptop

# Update laptop details (PUT)
@app.put("/laptops/{laptop_id}")
def update_laptop(laptop_id: int, updated_laptop: LaptopCreate, db: Session = Depends(get_db)):
    laptop = db.query(Laptop).filter(Laptop.LaptopID == laptop_id).first()
    if not laptop:
        raise HTTPException(status_code=404, detail="Laptop not found")

    for key, value in updated_laptop.dict().items():
        setattr(laptop, key, value)

    db.commit()
    db.refresh(laptop)
    return laptop

# Delete a laptop (DELETE)
@app.delete("/laptops/{laptop_id}")
def delete_laptop(session: Session, laptop_id: int):
    try:
        # Check if there are dependent records in pricehistory
        price_history_records = session.query(PriceHistory).filter_by(LaptopID=laptop_id).all()
        
        # If price history exists, delete them first
        if price_history_records:
            session.query(PriceHistory).filter_by(LaptopID=laptop_id).delete()
            session.commit()  # Commit to ensure foreign key constraint is not violated

        # Now delete the laptop
        laptop = session.query(Laptop).filter_by(LaptopID=laptop_id).first()
        if laptop:
            session.delete(laptop)
            session.commit()
            print(f"Laptop with ID {laptop_id} deleted successfully.")
        else:
            print(f"No laptop found with ID {laptop_id}.")
    
    except IntegrityError as e:
        session.rollback()  # Rollback in case of error
        print(f"Error deleting laptop: {e}")

# ----------------- Test Route -----------------
@app.get("/")
def home():
    return {"message": "FastAPI is working!"}
