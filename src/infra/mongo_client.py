import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(".env")

client = MongoClient(os.environ.get("MONGO_URI"))
