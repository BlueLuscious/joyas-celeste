import logging
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from front.services.views.subcategories_view_services import SubcategoriesViewService

logger = logging.getLogger(__name__)


class SubcategoriesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        template = loader.get_template("pages/subcategories.html")

        subcategories_view_service = SubcategoriesViewService()
        context = subcategories_view_service.get_context()

        return HttpResponse(template.render(context, request))
