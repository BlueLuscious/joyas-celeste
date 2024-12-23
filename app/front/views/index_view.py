import logging
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.template.backends.django import Template
from django.views import View
from front.services.views.index_view_service import IndexViewService

logger = logging.getLogger(__name__)


class IndexView(View):

    """ View for `index.html` template. """

    def get(self, request: HttpRequest) -> HttpResponse:
        template: Template = loader.get_template("pages/index.html")
        logger.info(f"Current template: {template.template.name}")

        index_view_service = IndexViewService()
        context = index_view_service.get_context()

        return HttpResponse(template.render(context, request))
    