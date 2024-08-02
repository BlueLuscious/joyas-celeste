from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.views import View
from front.models.product_model import ProductModel
from front.services.cart.shopping_cart import ShoppingCart

class ShoppingCartView(View):

    def post(self, request: HttpRequest, uuid: str) -> JsonResponse:
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            cart = ShoppingCart(request)
            product = ProductModel.objects.get(uuid=uuid)
            cart.add_to_cart(product)
            return JsonResponse({
                "cart": {
                    "total": cart.total(),
                    "items": cart.cart
                }
            }, status=201)
        else:
            return redirect("index")


    def delete(self, request: HttpRequest, uuid: str) -> JsonResponse:
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            cart = ShoppingCart(request)
            product = ProductModel.objects.get(uuid=uuid)
            cart.remove_from_cart(product)
            return JsonResponse({
                "cart": {
                    "total": cart.total(),
                    "items": cart.cart
                }
            }, status=200)
        else:
            return redirect("index")
