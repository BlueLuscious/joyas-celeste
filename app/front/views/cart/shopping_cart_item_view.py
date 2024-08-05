from django.http import HttpRequest, JsonResponse
from django.views import View
from front.services.cart.shopping_cart import ShoppingCart


class ShoppingCartItemView(View):

    def post(self, request: HttpRequest, action: str, uuid: str) -> JsonResponse:
        cart = ShoppingCart(request)
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
