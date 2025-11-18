import pytest
import os
import sys
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="module")
def db():
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    db = client["user_service_test"]
    yield db
    client.drop_database("user_service_test")
    client.close()
