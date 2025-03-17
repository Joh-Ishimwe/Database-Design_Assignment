from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

# Enum for OS (restricts values to valid options)
class OSEnum(str, Enum):
    windows = "Windows"
    macos = "MacOS"
    linux = "Linux"
    other = "Other"

# Schema for creating a laptop (SQL)
class LaptopCreate(BaseModel):
    Company: str = Field(..., min_length=1, max_length=100, description="Laptop brand")
    Product: str = Field(..., min_length=1, max_length=100, description="Laptop model")
    TypeName: str = Field(..., min_length=1, max_length=50, description="Type of laptop (e.g., Ultrabook, Gaming)")
    Inches: float = Field(..., gt=0, le=50, description="Screen size in inches")
    Weight: float = Field(..., gt=0, description="Weight of the laptop in kg")
    Price_euros: float = Field(..., gt=0, description="Price in euros, must be positive")
    OS: OSEnum  # Restricts OS to predefined options
    ScreenID: int = Field(..., gt=0, description="Must be a positive integer")
    CPU_ID: int = Field(..., gt=0, description="Must be a positive integer")
    GPU_ID: int = Field(..., gt=0, description="Must be a positive integer")
    StorageID: int = Field(..., gt=0, description="Must be a positive integer")

# Schema for updating a laptop (SQL)
class LaptopUpdate(BaseModel):
    Company: Optional[str] = Field(None, min_length=1, max_length=100, description="Laptop brand")
    Product: Optional[str] = Field(None, min_length=1, max_length=100, description="Laptop model")
    TypeName: Optional[str] = Field(None, min_length=1, max_length=50, description="Type of laptop")
    Inches: Optional[float] = Field(None, gt=0, le=50, description="Screen size in inches")
    Weight: Optional[float] = Field(None, gt=0, description="Weight must be positive")
    Price_euros: Optional[float] = Field(None, gt=0, description="Price must be positive")
    OS: Optional[OSEnum]
    ScreenID: Optional[int] = Field(None, gt=0, description="Must be a positive integer")
    CPU_ID: Optional[int] = Field(None, gt=0, description="Must be a positive integer")
    GPU_ID: Optional[int] = Field(None, gt=0, description="Must be a positive integer")
    StorageID: Optional[int] = Field(None, gt=0, description="Must be a positive integer")

# Schema for creating a laptop in MongoDB (NoSQL)
class LaptopNoSQLCreate(LaptopCreate):  # Reuse LaptopCreate validation
    pass

# Schema for updating a laptop in MongoDB (NoSQL)
class LaptopNoSQLUpdate(LaptopUpdate):  # Reuse LaptopUpdate validation
    pass
