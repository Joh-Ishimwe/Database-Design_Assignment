import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
if not MONGO_URL:
    raise ValueError("MONGO_URL is not set in the environment variables.")

# Test MongoDB connection
try:
    client = MongoClient(
        MONGO_URL,
        tls=True,  # Enable TLS/SSL
        tlsAllowInvalidCertificates=True  # Allow invalid certificates (for testing purposes)
    )
    db = client["laptops_db"]
    print("Connected to MongoDB successfully!")
    print("Available collections:", db.list_collection_names())
except Exception as e:
    print("Failed to connect to MongoDB:", e)