import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(".env")


def mongo_client_factory():
    database_name = "friends-gallery"
    return MongoClient(os.environ.get("MONGO_URI")), database_name
