import logging
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.views import View
from front.services.views.products_view_service import ProductsViewService

logger = logging.getLogger(__name__)


class ProductsView(View):
    def get(self, request: HttpRequest, page: int = 1) -> HttpResponse:
        template = loader.get_template("pages/products.html")
        logger.info(f"get template: {template.template.name}")

        page = request.GET.get("page")
        products_view_service = ProductsViewService()
        context = products_view_service.get_context(page)

        return HttpResponse(template.render(context, request))
