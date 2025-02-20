import random
from decimal import Decimal
from django.core.management import call_command
from django.templatetags.static import static
from django.test import TestCase
from front.templatetags.filters import product_filter
from product.models.category_model import CategoryModel
from product.models.product_model import ProductModel


class ProductFilterTest(TestCase):
    def setUp(self):
        call_command("loaddata", "seeds/category_seed.json")
        call_command("loaddata", "seeds/product_seed.json")
        self.categories = CategoryModel.objects.all()
        self.category = random.choice(self.categories)
        self.product = random.choice(ProductModel.objects.all())


    def test_convert_price_to_ARS(self):
        default_dollar = 1280
        converted_price = product_filter.convert_price_to_ARS(self.product.price, default_dollar)
        self.assertIsInstance(converted_price, Decimal)


    def test_format_number_AR(self):
        formatted_number = product_filter.format_number_AR(self.product.price)
        self.assertIsInstance(formatted_number, str)

        pattern = r'^\d{1,3}(?:\.\d{3})*(?:,\d{2})?$'
        self.assertRegex(formatted_number, pattern, "El formato del número no coincide con el formato esperado")
        