from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"
database = "gymnaut"

client = AsyncIOMotorClient(MONGO_DETAILS)
db = client["gymnaut"]

users = db.get_collection("users")
profiles = db.get_collection("profiles")