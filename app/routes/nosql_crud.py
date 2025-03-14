from fastapi import APIRouter, Depends
from app.services.nosql_services import (
    create_laptop_nosql,
    get_all_laptops_nosql,
    get_laptop_nosql,
    update_laptop_nosql,
    delete_laptop_nosql,
)
import logging
logger = logging.getLogger(__name__)
from fastapi import HTTPException
from app.schemas import LaptopNoSQLCreate, LaptopNoSQLUpdate
from app.database.nosql_db import get_nosql_collection
from pymongo.collection import Collection

router = APIRouter()

@router.post("/laptops/")
def create_laptop(laptop_data: LaptopNoSQLCreate, collection: Collection = Depends(get_nosql_collection)):
    try:
        # Call the service function to create the laptop
        inserted_laptop = create_laptop_nosql(collection, laptop_data)
        
        # Return a success response with the inserted data
        return {"message": "Laptop created successfully", "data": inserted_laptop}
    except HTTPException as e:
        # Re-raise HTTPException to return the error response
        raise e
    except Exception as e:
        # Handle unexpected errors
        logger.error(f"Unexpected error creating laptop: {e}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
    
@router.get("/laptops/")
def get_laptops(collection: Collection = Depends(get_nosql_collection)):
    return get_all_laptops_nosql(collection)

@router.get("/laptop/{laptop_id}")
def get_laptop(laptop_id: str, collection: Collection = Depends(get_nosql_collection)):
    return get_laptop_nosql(collection, laptop_id)

@router.put("/laptop/{laptop_id}")
def update_laptop(laptop_id: str, laptop_data: LaptopNoSQLUpdate, collection: Collection = Depends(get_nosql_collection)):
    return update_laptop_nosql(collection, laptop_id, laptop_data)

@router.delete("/laptop/{laptop_id}")
def delete_laptop(laptop_id: str, collection: Collection = Depends(get_nosql_collection)):
    return delete_laptop_nosql(collection, laptop_id)
