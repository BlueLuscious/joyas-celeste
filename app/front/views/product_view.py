import logging
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from front.services.views.product_view_service import ProductViewService

logger = logging.getLogger(__name__)


class ProductView(View):
    def get(self, request: HttpRequest, name: str = None) -> HttpResponse:
        template = loader.get_template("pages/product.html")
        logger.info(f"get template: {template.template.name}")

        product_view_service = ProductViewService()
        context = product_view_service.get_context(name)

        return HttpResponse(template.render(context, request))
