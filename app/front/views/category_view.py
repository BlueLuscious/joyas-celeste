import logging
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.template.backends.django import Template
from django.views import View
from front.services.views.category_view_service import CategoryViewService

logger = logging.getLogger(__name__)


class CategoryView(View):

    """ View for `category.html` template. """

    def get(self, request: HttpRequest, name: str) -> HttpResponse:
        template: Template = loader.get_template("pages/category.html")
        logger.info(f"Current template: {template.template.name}")

        category_view_service = CategoryViewService(name)
        context = category_view_service.get_context()

        return HttpResponse(template.render(context, request))
    