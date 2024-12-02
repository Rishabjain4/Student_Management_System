
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from decouple import config

# Read database configuration from environment variables
DATABASE_URL = config("DATABASE_URL")
DATABASE_NAME = config("DATABASE_NAME")

# Create a new client and connect to the server
client = MongoClient(DATABASE_URL, server_api=ServerApi('1'))

# client = MongoClient(uri, server_api=ServerApi('1'))
db = client[DATABASE_NAME]
student_collection = db["students"]
    