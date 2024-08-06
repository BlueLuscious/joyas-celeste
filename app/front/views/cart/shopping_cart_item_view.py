from django.http import HttpRequest, JsonResponse
from django.views import View
from front.services.cart.shopping_cart_service import ShoppingCartService


class ShoppingCartItemView(View):

    def post(self, request: HttpRequest, action: str, uuid: str) -> JsonResponse:
        cart = ShoppingCartService(request)
        if action == "add":
            cart.increment_quantity(uuid)
        if action == "subtract":
            cart.decrement_quantity(uuid)
            
        cart.save_cart()
        return JsonResponse({
            "cart": {
                "total": cart.total(),
                "items": cart.cart
            }
        }, status=200)
