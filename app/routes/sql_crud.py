from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.sql_db import get_db
from app.models.sql_models import Laptop, PriceHistory
from app.schemas import LaptopCreate, LaptopUpdate

# Initialize router
router = APIRouter()

# ---------------- CRUD Operations ----------------

# Create a new laptop (POST)
@router.post("/laptops/")
def create_laptop(laptop: LaptopCreate, db: Session = Depends(get_db)):
    new_laptop = Laptop(**laptop.dict())
    db.add(new_laptop)
    db.commit()
    db.refresh(new_laptop)
    return new_laptop

# Read all laptops (GET)
@router.get("/laptops/")
def get_laptops(db: Session = Depends(get_db)):
    return db.query(Laptop).all()

# Read a single laptop by ID (GET)
@router.get("/laptop/{laptop_id}")
def get_laptop(laptop_id: int, db: Session = Depends(get_db)):
    laptop = db.query(Laptop).filter(Laptop.LaptopID == laptop_id).first()
    if not laptop:
        raise HTTPException(status_code=404, detail="Laptop not found")
    return laptop

# Update laptop details (PUT)
@router.put("/laptop/{laptop_id}")
def update_laptop(laptop_id: int, updated_laptop: LaptopUpdate, db: Session = Depends(get_db)):
    laptop = db.query(Laptop).filter(Laptop.LaptopID == laptop_id).first()
    if not laptop:
        raise HTTPException(status_code=404, detail="Laptop not found")

    for key, value in updated_laptop.dict(exclude_unset=True).items():
        setattr(laptop, key, value)

    db.commit()
    db.refresh(laptop)
    return laptop

# Delete a laptop (DELETE)
@router.delete("/laptop/{laptop_id}")
def delete_laptop(laptop_id: int, db: Session = Depends(get_db)):
    # Delete price history records first
    db.query(PriceHistory).filter(PriceHistory.LaptopID == laptop_id).delete()
    
    # Delete the laptop
    laptop = db.query(Laptop).filter(Laptop.LaptopID == laptop_id).first()
    if not laptop:
        raise HTTPException(status_code=404, detail="Laptop not found")
    db.delete(laptop)
    db.commit()
    return {"message": f"Laptop with ID {laptop_id} deleted successfully."}