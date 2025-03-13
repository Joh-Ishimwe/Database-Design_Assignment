from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base



# Screen Table
class LaptopScreen(Base):
    __tablename__ = "laptopscreen"

    ScreenID = Column(Integer, primary_key=True, index=True)
    Screen = Column(String(50))
    ScreenW = Column(Integer)
    ScreenH = Column(Integer)
    Touchscreen = Column(String(10))
    IPSpanel = Column(String(10))
    RetinaDisplay = Column(String(10))

# CPU Table
class CPU(Base):
    __tablename__ = "CPU"

    CPU_ID = Column(Integer, primary_key=True, index=True)
    CPU_company = Column(String(50))
    CPU_freq = Column(Float)
    CPU_model = Column(String(100))

# GPU Table
class GPU(Base):
    __tablename__ = "GPU"

    GPU_ID = Column(Integer, primary_key=True, index=True)
    GPU_company = Column(String(50))
    GPU_model = Column(String(100))

# Storage Table
class Storage(Base):
    __tablename__ = "storage"

    StorageID = Column(Integer, primary_key=True, index=True)
    PrimaryStorage = Column(Integer)
    PrimaryStorageType = Column(String(50))
    SecondaryStorage = Column(Integer, nullable=True)
    SecondaryStorageType = Column(String(50), nullable=True)

# Laptop Table
class Laptop(Base):
    __tablename__ = "laptop"

    LaptopID = Column(Integer, primary_key=True, index=True)
    Company = Column(String(50))
    Product = Column(String(100))
    TypeName = Column(String(50))
    Inches = Column(Float)
    Weight = Column(Float)
    Price_euros = Column(Float)
    OS = Column(String(50))

    ScreenID = Column(Integer, ForeignKey("laptopscreen.ScreenID"))
    CPU_ID = Column(Integer, ForeignKey("CPU.CPU_ID"))
    GPU_ID = Column(Integer, ForeignKey("GPU.GPU_ID"))
    StorageID = Column(Integer, ForeignKey("storage.StorageID"))

# Price History Table
class PriceHistory(Base):
    __tablename__ = "pricehistory"

    LogID = Column(Integer, primary_key=True, index=True)
    LaptopID = Column(Integer, ForeignKey("laptop.LaptopID", ondelete="CASCADE"))
    OldPrice = Column(Float)
    NewPrice = Column(Float)
    ChangeDate = Column(TIMESTAMP)
