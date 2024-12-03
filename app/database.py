
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Read database configuration from environment variables
MONGODB_URL = "mongodb+srv://rishabjain0411:WggbMVStEft1pTSG@m0-cluster-atlas.giqqf.mongodb.net/"
MONGODB_NAME = "Student"

# Create a new client and connect to the server
client = MongoClient(MONGODB_URL, server_api=ServerApi('1'))

# client = MongoClient(uri, server_api=ServerApi('1'))
db = client[MONGODB_NAME]
student_collection = db["students"]
    
