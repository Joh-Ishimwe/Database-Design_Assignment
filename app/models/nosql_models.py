from pydantic import BaseModel
from typing import Optional

class LaptopNoSQLCreate(BaseModel):
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

class LaptopNoSQLUpdate(BaseModel):
    Company: Optional[str] = None
    Product: Optional[str] = None
    TypeName: Optional[str] = None
    Inches: Optional[float] = None
    Weight: Optional[float] = None
    Price_euros: Optional[float] = None
    OS: Optional[str] = None
    ScreenID: Optional[int] = None
    CPU_ID: Optional[int] = None
    GPU_ID: Optional[int] = None
    StorageID: Optional[int] = None