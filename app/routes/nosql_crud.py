from fastapi import APIRouter, Depends, HTTPException
from app.services.nosql_services import (
    create_laptop_nosql,
    get_all_laptops_nosql,
    get_laptop_nosql,
    update_laptop_nosql,
    delete_laptop_nosql,
)
from app.schemas import LaptopNoSQLCreate, LaptopNoSQLUpdate
from app.database.nosql_db import get_nosql_collection
from pymongo.collection import Collection

router = APIRouter()

@router.post("/laptops/")
def create_laptop(laptop_data: LaptopNoSQLCreate, collection: Collection = Depends(get_nosql_collection)):
    try:
        result = create_laptop_nosql(collection, laptop_data)
        return {"message": "Laptop created successfully", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/laptops/")
def get_laptops(collection: Collection = Depends(get_nosql_collection)):
    try:
        laptops = get_all_laptops_nosql(collection)
        return {"message": "Laptops retrieved successfully", "data": laptops}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/laptop/{laptop_id}")
def get_laptop(laptop_id: str, collection: Collection = Depends(get_nosql_collection)):
    try:
        laptop = get_laptop_nosql(collection, laptop_id)
        if not laptop:
            raise HTTPException(status_code=404, detail="Laptop not found")
        return {"message": "Laptop retrieved successfully", "data": laptop}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/laptop/{laptop_id}")
def update_laptop(laptop_id: str, laptop_data: LaptopNoSQLUpdate, collection: Collection = Depends(get_nosql_collection)):
    try:
        updated = update_laptop_nosql(collection, laptop_id, laptop_data)
        if not updated:
            raise HTTPException(status_code=404, detail="Laptop not found")
        return {"message": f"Laptop with ID {laptop_id} updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/laptop/{laptop_id}")
def delete_laptop(laptop_id: str, collection: Collection = Depends(get_nosql_collection)):
    try:
        deleted = delete_laptop_nosql(collection, laptop_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Laptop not found")
        return {"message": f"Laptop with ID {laptop_id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))