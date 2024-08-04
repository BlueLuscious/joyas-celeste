from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.views import View
from front.models.product_model import ProductModel
from front.services.cart.shopping_cart import ShoppingCart

class ShoppingCartView(View):

    def post(self, request: HttpRequest, action: str, uuid: str) -> JsonResponse:
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            cart = ShoppingCart(request)
            if action == "add":
                product = ProductModel.objects.get(uuid=uuid)
                cart.add_to_cart(product)
            if action == "remove":
                key = uuid.split("_")
                cart.remove_from_cart(key[0], key[1])

            return JsonResponse({
                "cart": {
                    "total": cart.total(),
                    "items": cart.cart
                }
            }, status=201)
        else:
            return redirect("index")
