import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user


def test_serialize_user_completo():
    user = {
        "email": "teste@xpto.com",
        "name": "Teste Xpto",
        "address": "123 Rua A",
        "role": "admin",
    }
    resultado = serialize_user(user)
    esperado = {
        "email": "teste@xpto.com",
        "name": "Teste Xpto",
        "address": "123 Rua A",
        "role": "admin",
    }

    assert resultado == esperado


def test_serialize_user_email():
    user = {
        "email": "teste@xpto.com",
    }
    resultado = serialize_user(user)
    esperado = {
        "email": "teste@xpto.com",
        "name": "",
        "address": "",
        "role": "cliente",
    }

    assert resultado == esperado


def test_serialize_user_null():
    user = {}
    resultado = serialize_user(user)
    esperado = {
        "email": None,
        "name": "",
        "address": "",
        "role": "cliente",
    }

    assert resultado == esperado


def test_serialize_user_inteiro():
    with pytest.raises(AttributeError):
        serialize_user(12345)


def test_serialize_user_string():
    with pytest.raises(AttributeError):
        serialize_user("usuario_invalido")


def test_serialize_user_inesperado():
    user = {
        "email": 1203,
        "name": ["Nome", "Invalido"],
        "address": {"rua": "123"},
        "role": True,
    }
    resultado = serialize_user(user)
    esperado = {
        "email": 1203,
        "name": ["Nome", "Invalido"],
        "address": {"rua": "123"},
        "role": True,
    }

    assert resultado == esperado