from bson import ObjectId
from pymongo.collection import Collection
from app.schemas import LaptopNoSQLCreate, LaptopNoSQLUpdate

def create_laptop_nosql(collection: Collection, laptop_data: LaptopNoSQLCreate):
    laptop_dict = laptop_data.dict()
    result = collection.insert_one(laptop_dict)
    return {"_id": str(result.inserted_id), **laptop_dict}

def get_laptop_nosql(collection: Collection, laptop_id: str):
    try:
        laptop = collection.find_one({"_id": ObjectId(laptop_id)})
        if laptop:
            laptop["_id"] = str(laptop["_id"])
        return laptop
    except Exception:
        return {"error": "Invalid ObjectId format"}

def get_all_laptops_nosql(collection: Collection):
    laptops = list(collection.find({}))
    for laptop in laptops:
        laptop["_id"] = str(laptop["_id"])
    return laptops

def update_laptop_nosql(collection: Collection, laptop_id: str, laptop_data: LaptopNoSQLUpdate):
    try:
        update_data = {k: v for k, v in laptop_data.dict().items() if v is not None}
        result = collection.update_one({"_id": ObjectId(laptop_id)}, {"$set": update_data})
        return result.modified_count > 0
    except Exception:
        return {"error": "Invalid ObjectId format"}

def delete_laptop_nosql(collection: Collection, laptop_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(laptop_id)})
        return result.deleted_count > 0
    except Exception:
        return {"error": "Invalid ObjectId format"}