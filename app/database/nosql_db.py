import os
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi  # Import certifi for SSL certificates

# Load environment variables from .env file
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
if not MONGO_URL:
    raise ValueError("MONGO_URL is not set in the environment variables.")

# Configure SSL/TLS
client = MongoClient(
    MONGO_URL,
    tls=True,  # Enable TLS/SSL
    tlsCAFile=certifi.where(),  # Use certifi's CA bundle
    tlsAllowInvalidCertificates=False  # Disallow invalid certificates
)

db = client["laptops_db"]

def get_nosql_collection():
    return db["laptops"]