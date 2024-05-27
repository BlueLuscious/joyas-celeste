from django.test import TestCase, Client
from django.urls import reverse


class CategoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_template(self):
        response = self.client.get(reverse('categories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/category.html')
