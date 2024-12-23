import logging
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.template.backends.django import Template
from django.views import View
from front.services.views.subcategory_view_service import SubcategoryViewService

logger = logging.getLogger(__name__)


class SubcategoryView(View):

    """ View for `subcategory.html` template. """

    def get(self, request: HttpRequest, name: str, sub_name: str) -> HttpResponse:
        template: Template = loader.get_template("pages/subcategory.html")
        logger.info(f"Current template: {template.template.name}")
        
        subcategory_view_service = SubcategoryViewService(name, sub_name)
        context = subcategory_view_service.get_context()

        return HttpResponse(template.render(context, request))
    