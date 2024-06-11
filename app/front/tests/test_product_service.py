import random
from django.core.management import call_command
from django.test import TestCase
from front.services.product_service import ProductService
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel


class ProductServiceTest(TestCase):
    def setUp(self):
        call_command("loaddata", "seeds/category_seed.json")
        call_command("loaddata", "seeds/product_seed.json")
        self.categories = CategoryModel.objects.all()
        self.category = random.choice(self.categories)
        self.products_by_category = ProductModel.objects.filter(category=self.category)
        self.default_page = 1
        self.default_products_by_page = 12 


    def test_get_random_products_for_each_category(self):
        random_products = ProductService.get_random_products_for_each_category(self.categories, 10)
        self.assertLessEqual(len(random_products), len(self.categories) * 10)


    def test_paginate_products(self):
        pagination = ProductService.paginate_products(self.products_by_category, self.default_page, self.default_products_by_page)
        products_page = pagination.get("products_page")
        
        self.assertEqual(products_page.number, self.default_page)
        self.assertLessEqual(len(products_page), self.default_products_by_page)
