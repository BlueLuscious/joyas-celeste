import logging
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.views import View
from front.services.category_service import CategoryService
from typing import Optional

logger = logging.getLogger(__name__)

class CategoryView(View):
    def get(self, request: HttpRequest, name: Optional[str] = None) -> HttpResponse:
        category_service = CategoryService()
        
        template = category_service.get_template(name)
        context = category_service.get_context(name)

        return HttpResponse(template.render(context, request))
