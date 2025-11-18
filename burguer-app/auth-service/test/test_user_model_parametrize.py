import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.user_model import serialize_user


@pytest.mark.parametrize(
    "user, esperado",
    [
        (
            {
                "email": "teste@xpto.com",
                "name": "Teste Xpto",
                "address": "123 Rua A",
                "role": "admin",
            },
            {
                "email": "teste@xpto.com",
                "name": "Teste Xpto",
                "address": "123 Rua A",
                "role": "admin",
            },
        ),
        (
            {
                "email": "teste@xpto.com",
            },
            {
                "email": "teste@xpto.com",
                "name": "",
                "address": "",
                "role": "cliente",
            },
        ),
        (
            {},
            {
                "email": None,
                "name": "",
                "address": "",
                "role": "cliente",
            },
        ),
        (
            {
                "email": 1203,
                "name": ["Nome", "Invalido"],
                "address": {"rua": "123"},
                "role": True,
            },
            {
                "email": 1203,
                "name": ["Nome", "Invalido"],
                "address": {"rua": "123"},
                "role": True,
            },
        ),
    ],
)
def test_serialize_user(user, esperado):
    resultado = serialize_user(user)
    assert resultado == esperado


@pytest.mark.parametrize("entrada", [None, "string", 123, []])
def test_serialize_user_inesperado(entrada):
    with pytest.raises(AttributeError):
        serialize_user(entrada)
