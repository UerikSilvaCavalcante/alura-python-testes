import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user


@pytest.mark.usefixtures("db")
def test_conexao_banco(db):
    resultado = db.list_collection_names()
    assert isinstance(resultado, list)
