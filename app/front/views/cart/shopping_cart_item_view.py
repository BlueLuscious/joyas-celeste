from django.http import HttpRequest, JsonResponse
from django.views import View
from front.services.cart.shopping_cart import ShoppingCart


class ShoppingCartItemView(View):

    def post(self, request: HttpRequest, action: str, uuid: str) -> JsonResponse:
        key = uuid.split("_")
        if action == "add":
            cart = ShoppingCart(request)
            cart.increment_quantity(key[0], 1, key[1])
        if action == "subtract":
            cart = ShoppingCart(request)
            cart.decrement_quantity(key[0], 1, key[1])
            
        cart.save_cart()
        return JsonResponse({
                "cart": {
                    "total": cart.total(),
                    "items": cart.cart
                }
        }, status=200)
