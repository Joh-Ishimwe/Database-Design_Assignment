from bson import ObjectId
from pymongo.collection import Collection
from app.schemas import LaptopNoSQLCreate, LaptopNoSQLUpdate
import logging
from fastapi import HTTPException

# Set up logging
logger = logging.getLogger(__name__)


def create_laptop_nosql(collection: Collection, laptop_data: LaptopNoSQLCreate):
    try:
        # Convert Pydantic model to dictionary
        laptop_dict = laptop_data.dict()
        
        # Insert the document into the collection
        result = collection.insert_one(laptop_dict)
        
        # Convert ObjectId to string and return the inserted document
        inserted_laptop = {**laptop_dict, "_id": str(result.inserted_id)}
        return inserted_laptop
    except Exception as e:
        logger.error(f"Error creating laptop: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to create laptop: {str(e)}")
    
def get_laptop_nosql(collection: Collection, laptop_id: str):
    try:
        # Find the document by ID
        laptop = collection.find_one({"_id": ObjectId(laptop_id)})
        if not laptop:
            raise HTTPException(status_code=404, detail="Laptop not found")
        
        # Convert ObjectId to string
        laptop["_id"] = str(laptop["_id"])
        return laptop
    except Exception as e:
        logger.error(f"Error fetching laptop: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to fetch laptop: {str(e)}")
    
def get_all_laptops_nosql(collection: Collection):
    try:
        # Fetch all documents
        laptops = list(collection.find({}))
        
        # Convert ObjectId to string for each document
        for laptop in laptops:
            laptop["_id"] = str(laptop["_id"])
        return laptops
    except Exception as e:
        logger.error(f"Error fetching all laptops: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to fetch laptops: {str(e)}")
    
def update_laptop_nosql(collection: Collection, laptop_id: str, laptop_data: LaptopNoSQLUpdate):
    try:
        update_data = {k: v for k, v in laptop_data.dict().items() if v is not None}
        result = collection.update_one({"_id": ObjectId(laptop_id)}, {"$set": update_data})
        return result.modified_count > 0
    except Exception as e:
        logger.error(f"Error updating laptop: {e}")
        raise Exception("Failed to update laptop")

def delete_laptop_nosql(collection: Collection, laptop_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(laptop_id)})
        return result.deleted_count > 0
    except Exception as e:
        logger.error(f"Error deleting laptop: {e}")
        raise Exception("Failed to delete laptop")