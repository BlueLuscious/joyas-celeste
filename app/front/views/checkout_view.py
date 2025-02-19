import logging
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.template.backends.django import Template
from django.views import View
from cart.models.cart_model import CartModel

logger = logging.getLogger(__name__)


class CheckoutView(View):

    """ View for `checkout.html` template. """

    def get(self, request: HttpRequest) -> HttpResponse:
        template: Template = loader.get_template("pages/checkout.html")
        logger.info(f"get template: {template.template.name}")

        cart_model = CartModel.objects.filter(user=request.user).last()
        cart_items = cart_model.items.all()

        context = {
            "cart": cart_model,
            "cart_items": cart_items,
        }
        return HttpResponse(template.render(context, request))
    