from django.test import TestCase
from back.services.cripto_ya_service import CriptoYaService


class CriptoYaServiceTest(TestCase):

    def test_get_dollar_quotes_OK(self):
        cripto_ya_service = CriptoYaService()
        dollar_quotes = cripto_ya_service.get_dollar_quotes()
        self.assertTrue(dollar_quotes)
