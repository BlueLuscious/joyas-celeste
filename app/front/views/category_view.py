import logging
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.views import View
from front.models.category_model import CategoryModel
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)

class CategoryView(View):
    def get(self, request, name=None):
        template = loader.get_template("pages/category.html")
        logger.info(f"get template: {template.template.name}")

        if name is None:
            categories = CategoryModel.objects.all()
            products = ProductModel.objects.all()

            context = {
                "categories": categories,
                "products": products,
            }
        else:
            category = CategoryModel.objects.get(name=name.capitalize())
            products = ProductModel.objects.filter(category=category)

            context = {
                "category": category,
                "products": products,
            }

        return HttpResponse(template.render(context, request))
