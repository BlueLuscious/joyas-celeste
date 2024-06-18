import random
from django.core.management import call_command
from django.template import Context, Template
from django.test import TestCase
from django.urls import reverse
from front.models.category_model import CategoryModel


class IndexTagTest(TestCase):
    def setUp(self):
        call_command("loaddata", "seeds/category_seed.json")
        

    def test_category_card_tag(self):
        category_name = random.choice(CategoryModel.objects.all()).name
        category_url = reverse("category", kwargs={"name": category_name.capitalize()})
        
        template = Template("{% load index_tag %}{% category_card category_url category_name %}")
        context = Context({"category_url": category_url, "category_name": category_name})
        rendered = template.render(context)
        
        self.assertIn(category_url, rendered)
        self.assertIn(category_name, rendered)
