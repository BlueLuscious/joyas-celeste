import logging
from django.core.cache import cache
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.template.backends.django import Template
from django.views import View
from back.services.mercado_pago_service import MercadoPagoService
from cart.models.cart_item_model import CartItemModel

logger = logging.getLogger(__name__)


class CheckoutView(View):
    
    def get(self, request: HttpRequest) -> HttpResponse:
        template: Template = loader.get_template("pages/checkout.html")
        logger.info(f"get template: {template.template.name}")

        dollar_blue_ask: float | None = cache.get("dollar_blue_ask")
        cart_items = CartItemModel.objects.filter(user=request.user)
        mp_service = MercadoPagoService()
        preference = mp_service.create_preference(cart_items, dollar_blue_ask)

        context = {
            "cart_items": cart_items,
            "preference": preference,
            "public_key": mp_service.public_key,
        }

        return HttpResponse(template.render(context, request))
