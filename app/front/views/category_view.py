import logging
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.views import View
from front.services.category_service import CategoryService

logger = logging.getLogger(__name__)

class CategoryView(View):
    def get(self, request, name=None):
        category_service = CategoryService()
        
        template = category_service.get_template(name)
        context = category_service.get_context(name)

        return HttpResponse(template.render(context, request))
