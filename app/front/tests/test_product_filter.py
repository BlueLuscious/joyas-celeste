import random
from django.core.management import call_command
from django.templatetags.static import static
from django.test import TestCase
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel
from front.services.product_service import ProductService
from front.templatetags import product_filter


class ProductFilterTest(TestCase):
    def setUp(self):
        call_command("loaddata", "seeds/category_seed.json")
        call_command("loaddata", "seeds/product_seed.json")
        self.categories = CategoryModel.objects.all()
        self.category = random.choice(self.categories)
        self.product = random.choice(ProductModel.objects.all())


    def test_products_by_category(self):
        products = ProductService.get_random_products_for_each_category(self.categories, 10)
        filtered_products = product_filter.products_by_category(products, self.category)
        self.assertLessEqual(len(filtered_products), 10)
        self.assertTrue(all(product.category == self.category for product in filtered_products))


    def test_format_number(self):
        formatted_number = product_filter.format_number(self.product.price)
        self.assertIsInstance(formatted_number, str)

        pattern = r'^\d{1,3}(?:\.\d{3})*(?:,\d{2})?$'
        self.assertRegex(formatted_number, pattern, "El formato del número no coincide con el formato esperado")


    def test_image_or_default(self):
        url = product_filter.image_or_default(self.product.image)

        if self.product.image:
            self.assertEqual(url, self.product.image.url)
        else:
            self.assertEqual(url, static("images/default-no-image.png"))
