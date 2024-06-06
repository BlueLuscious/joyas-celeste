import logging
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from front.services.index_service import IndexService

logger = logging.getLogger(__name__)

class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        template = loader.get_template("pages/index.html")
        logger.info(f"get template: {template.template.name}")

        index_service = IndexService()
        context = index_service.get_context()

        return HttpResponse(template.render(context, request))
