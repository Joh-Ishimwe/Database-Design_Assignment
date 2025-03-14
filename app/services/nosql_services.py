from bson import ObjectId
from pymongo.collection import Collection
from app.schemas import LaptopNoSQLCreate, LaptopNoSQLUpdate
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_laptop_nosql(collection: Collection, laptop_data: LaptopNoSQLCreate):
    try:
        laptop_dict = laptop_data.dict()
        result = collection.insert_one(laptop_dict)
        return {"_id": str(result.inserted_id), **laptop_dict}
    except Exception as e:
        logger.error(f"Error creating laptop: {e}")
        raise

def get_laptop_nosql(collection: Collection, laptop_id: str):
    try:
        laptop = collection.find_one({"_id": ObjectId(laptop_id)})
        if laptop:
            laptop["_id"] = str(laptop["_id"])
        return laptop
    except Exception as e:
        logger.error(f"Error fetching laptop: {e}")
        return {"error": "Invalid ObjectId format"}

def get_all_laptops_nosql(collection: Collection):
    try:
        laptops = list(collection.find({}))
        for laptop in laptops:
            laptop["_id"] = str(laptop["_id"])
        return laptops
    except Exception as e:
        logger.error(f"Error fetching all laptops: {e}")
        raise

def update_laptop_nosql(collection: Collection, laptop_id: str, laptop_data: LaptopNoSQLUpdate):
    try:
        update_data = {k: v for k, v in laptop_data.dict().items() if v is not None}
        result = collection.update_one({"_id": ObjectId(laptop_id)}, {"$set": update_data})
        return result.modified_count > 0
    except Exception as e:
        logger.error(f"Error updating laptop: {e}")
        raise

def delete_laptop_nosql(collection: Collection, laptop_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(laptop_id)})
        return result.deleted_count > 0
    except Exception as e:
        logger.error(f"Error deleting laptop: {e}")
        raise