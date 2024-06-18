import random
from django.core.management import call_command
from django.test import TestCase, Client
from django.urls import reverse
from front.models.category_model import CategoryModel


class CategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        call_command("loaddata", "seeds/category_seed.json")


    def test_get_categories_template(self):
        response = self.client.get(reverse("categories"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/categories.html")


    def test_get_category_template(self):
        category = random.choice(CategoryModel.objects.all())
        
        if category:
            response = self.client.get(reverse("category", kwargs={"name": category.name.capitalize()}))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "pages/category.html")
        else:
            self.fail("No category found in the database.")
