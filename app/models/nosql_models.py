from pydantic import BaseModel
from typing import Optional

class LaptopNoSQLCreate(BaseModel):
    brand: str
    model: str
    processor: str
    ram: int
    storage: int
    price: float

class LaptopNoSQLUpdate(BaseModel):
    brand: Optional[str] = None
    model: Optional[str] = None
    processor: Optional[str] = None
    ram: Optional[int] = None
    storage: Optional[int] = None
    price: Optional[float] = None
