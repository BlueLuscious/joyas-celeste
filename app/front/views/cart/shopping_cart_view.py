from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.views import View
from front.models.product_model import ProductModel
from front.services.cart.shopping_cart import ShoppingCart

class ShoppingCartView(View):

    def post(self, request: HttpRequest, action: str, uuid: str) -> JsonResponse:
        cart = ShoppingCart(request)
        if action == "add":
            product = ProductModel.objects.get(uuid=uuid)
            cart.add_to_cart(product)
        if action == "remove":
            cart.remove_from_cart(uuid)

        return JsonResponse({
            "cart": {
                "total": cart.total(),
                "items": cart.cart
            }
        }, status=201)

