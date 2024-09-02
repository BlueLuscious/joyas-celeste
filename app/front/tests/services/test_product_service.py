import random
from django.core.management import call_command
from django.test import TestCase
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel
from front.services.product_service import ProductService


class ProductServiceTest(TestCase):
    def setUp(self):
        call_command("loaddata", "seeds/category_seed.json")
        call_command("loaddata", "seeds/product_seed.json")
        self.categories = CategoryModel.objects.all()
        self.category = random.choice(self.categories)
        self.products_by_category = ProductModel.objects.filter(category=self.category)


    def test_paginate_products(self):
        default_page = 1
        default_products_by_page = 12
        default_total_pages = 5
        
        pagination = ProductService.paginate_products(self.products_by_category, default_page, default_products_by_page)
        products_page = pagination.get("products_page")
        page_numbers = pagination.get("page_numbers")
        
        self.assertEqual(products_page.number, default_page)
        self.assertLessEqual(len(products_page), default_products_by_page)
        self.assertLessEqual(len(page_numbers), default_total_pages)
