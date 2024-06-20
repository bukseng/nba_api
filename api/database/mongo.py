import os

from dotenv import load_dotenv
import pymongo

load_dotenv()

def get_mongo_client() -> pymongo.MongoClient:
    return pymongo.MongoClient(os.getenv("MONGODB_URI"))


def get_mongo_db() -> pymongo.database.Database:
    return get_mongo_client()[os.getenv("DB_NAME")]


def get_mongo_coll(coll_name: str) -> pymongo.collection.Collection:
    return get_mongo_db()[coll_name]
