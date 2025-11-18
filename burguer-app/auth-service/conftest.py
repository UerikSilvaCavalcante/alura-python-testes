import pytest
import os
import sys
from pymongo import MongoClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def mongo_client():
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    yield client
    client.close()


@pytest.fixture(scope="function")
def test_db(mongo_client):
    db = mongo_client["burguer_app_db"]
    db["users"].delete_many({})
    db["orders"].delete_many({})
    yield db
    