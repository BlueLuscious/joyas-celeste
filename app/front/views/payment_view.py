import logging
from django.core.cache import cache
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.template.backends.django import Template
from django.views import View
from back.services.mercado_pago_service import MercadoPagoService
from cart.models.cart_model import CartModel
from order.models.order_item_model import OrderItemModel
from order.models.order_model import OrderModel

logger = logging.getLogger(__name__)


class PaymentView(View):

    """ View for `payment.html` template. """
    
    def post(self, request: HttpRequest) -> HttpResponse:
        template: Template = loader.get_template("pages/payment.html")
        logger.info(f"get template: {template.template.name}")

        dollar_blue_ask: float | None = cache.get("dollar_blue_ask")
        if not dollar_blue_ask:
            logger.error("Ocurrio un problema al obtener la cotizacion, intente nuevamente")
            return redirect(request.META.get("HTTP_REFERER"))

        cart_model = CartModel.objects.filter(user=request.user).last()
        cart_items = cart_model.items.all()


        # TODO: Create order and order item.
        OrderModel.objects.all().delete()
        if cart_items:
            order = OrderModel.create_order(request.user)
            order.save()
            for item in cart_items:
                order_item = OrderItemModel.create_order_item(item, order)
                order_item.save()


        mp_service = MercadoPagoService()
        preference = mp_service.create_preference(cart_items, dollar_blue_ask) 

        context = {
            "order": order,
            "preference": preference,
            "public_key": mp_service.public_key,
        }

        return HttpResponse(template.render(context, request))
    