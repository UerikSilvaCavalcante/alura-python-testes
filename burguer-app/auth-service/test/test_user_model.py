import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user, UserModel


class TestUserModel(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente de teste"""
        self.user_data = UserModel(
            email="teste@exemplo.com",
            name="Test User",
            address="123 Test St",
            role="cliente",
        )

    def tearDown(self):
        """Limpa o ambiente de teste"""
        self.user_data = None

    def test_to_dict(self):
        """Testa a conversao do modelo para o dicionario"""
        expected = {
            "email": "teste@exemplo.com",
            "name": "Test User",
            "address": "123 Test St",
            "role": "cliente",
        }
        self.assertEqual(self.user_data.to_dict(), expected)  # type: ignore

    def test_serialize_user_incompleto(self):
        result = self.user_data.serialize()  # type: ignore
        self.assertEqual(result["email"], "teste@exemplo.com")
        self.assertEqual(result["name"], "Test User")
        self.assertEqual(result["address"], "123 Test St")
        self.assertEqual(result["role"], "cliente")
        self.assertNotIn("password", result)

    def test_assert_raises_exemple(self):
        def rais_error():
            raise ValueError("Exemplo de erro")

        with self.assertRaises(ValueError):
            rais_error()
