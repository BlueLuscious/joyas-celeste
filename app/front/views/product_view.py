import logging
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.template.backends.django import Template
from django.views import View
from front.services.views.product_view_service import ProductViewService

logger = logging.getLogger(__name__)


class ProductView(View):

    """ View for `product.html` template. """

    def get(self, request: HttpRequest, name: str = None) -> HttpResponse:
        template: Template = loader.get_template("pages/product.html")
        logger.info(f"Current template: {template.template.name}")

        product_view_service = ProductViewService(name)
        context = product_view_service.get_context()

        return HttpResponse(template.render(context, request))
    