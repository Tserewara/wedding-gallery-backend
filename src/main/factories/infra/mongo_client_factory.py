import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(".env")


def mongo_client_factory():
    database_name = "friends-gallery"
    MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
    connection_string = f"mongodb+srv://tserewara:{MONGO_PASSWORD}@cluster0.fizpd.mongodb.net/friends-gallery?retryWrites=true&w=majority"
    return MongoClient(connection_string), database_name
