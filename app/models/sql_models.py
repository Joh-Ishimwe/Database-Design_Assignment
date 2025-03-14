from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database.sql_db import Base  # Import Base from sql_db.py

# Screen Table
class LaptopScreen(Base):
    __tablename__ = "laptopscreen"

    ScreenID = Column(Integer, primary_key=True, index=True)
    Screen = Column(String(50), nullable=False)
    ScreenW = Column(Integer)
    ScreenH = Column(Integer)
    Touchscreen = Column(String(10))
    IPSpanel = Column(String(10))
    RetinaDisplay = Column(String(10))

    # Relationship to Laptop
    laptops = relationship("Laptop", back_populates="screen")

# CPU Table
class CPU(Base):
    __tablename__ = "cpu"

    CPU_ID = Column(Integer, primary_key=True, index=True)
    CPU_company = Column(String(50), nullable=False)
    CPU_freq = Column(Float, nullable=False)
    CPU_model = Column(String(100), nullable=False)

    # Relationship to Laptop
    laptops = relationship("Laptop", back_populates="cpu")

# GPU Table
class GPU(Base):
    __tablename__ = "gpu"

    GPU_ID = Column(Integer, primary_key=True, index=True)
    GPU_company = Column(String(50), nullable=False)
    GPU_model = Column(String(100), nullable=False)

    # Relationship to Laptop
    laptops = relationship("Laptop", back_populates="gpu")

# Storage Table
class Storage(Base):
    __tablename__ = "storage"

    StorageID = Column(Integer, primary_key=True, index=True)
    PrimaryStorage = Column(Integer, nullable=False)
    PrimaryStorageType = Column(String(50), nullable=False)
    SecondaryStorage = Column(Integer, nullable=True)
    SecondaryStorageType = Column(String(50), nullable=True)

    # Relationship to Laptop
    laptops = relationship("Laptop", back_populates="storage")

# Laptop Table
class Laptop(Base):
    __tablename__ = "laptop"

    LaptopID = Column(Integer, primary_key=True, index=True)
    Company = Column(String(50), nullable=False)
    Product = Column(String(100), nullable=False)
    TypeName = Column(String(50), nullable=False)
    Inches = Column(Float, nullable=False)
    Weight = Column(Float, nullable=True)
    Price_euros = Column(Float, nullable=False)
    OS = Column(String(50), nullable=True)

    # Foreign Keys
    ScreenID = Column(Integer, ForeignKey("laptopscreen.ScreenID", ondelete="SET NULL"))
    CPU_ID = Column(Integer, ForeignKey("cpu.CPU_ID", ondelete="SET NULL"))
    GPU_ID = Column(Integer, ForeignKey("gpu.GPU_ID", ondelete="SET NULL"))
    StorageID = Column(Integer, ForeignKey("storage.StorageID", ondelete="SET NULL"))

    # Relationships
    screen = relationship("LaptopScreen", back_populates="laptops")
    cpu = relationship("CPU", back_populates="laptops")
    gpu = relationship("GPU", back_populates="laptops")
    storage = relationship("Storage", back_populates="laptops")

# Price History Table
class PriceHistory(Base):
    __tablename__ = "pricehistory"

    LogID = Column(Integer, primary_key=True, index=True)
    LaptopID = Column(Integer, ForeignKey("laptop.LaptopID", ondelete="CASCADE"))
    OldPrice = Column(Float, nullable=False)
    NewPrice = Column(Float, nullable=False)
    ChangeDate = Column(TIMESTAMP, nullable=False)