from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
MONGODB_URI = f"""{os.getenv("MONGO_URI")}/?retryWrites=true&w=majority"""
COLLECTION = f"""{os.getenv("MONGO_COLLECTION")}"""
DATABASE = f"""{os.getenv("MONGO_DATABASE")}"""

# Create a new client and connect to the server
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))
db = client[DATABASE]
collection_name = db[COLLECTION]
