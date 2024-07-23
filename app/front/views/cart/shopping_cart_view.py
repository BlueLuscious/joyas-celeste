from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from front.models.product_model import ProductModel
from front.services.cart.shopping_cart import ShoppingCart

class ShoppingCartView(View):

    def post(self, request, uuid):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            cart = ShoppingCart(request)
            product = get_object_or_404(ProductModel, uuid=uuid)
            quantity = int(request.POST.get('quantity', 1))
            cart.add_to_cart(product, quantity)
            return JsonResponse({
                'cart': {
                    'total': cart.total(),
                    'items': cart.cart
                }
            }, status=200)
        else:
            return redirect('index')


    def delete(self, request, uuid):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            cart = ShoppingCart(request)
            product = get_object_or_404(ProductModel, uuid=uuid)
            cart.remove_from_cart(product)
            return JsonResponse({
                'cart': {
                    'total': cart.total(),
                    'items': cart.cart
                }
            }, status=200)
        else:
            return redirect('index')
        

    # def update_product(self, request, uuid):
    #     carrito = ShoppingCart(request)
    #     producto = get_object_or_404(ProductModel, uuid=uuid)
    #     cantidad = int(request.POST.get('cantidad'))
    #     carrito.update_cart(producto, cantidad)
    #     return redirect('index')

    # def carrito_detalle(request):
    #     carrito = ShoppingCart(request)
    #     return render(request, 'carrito/detalle.html', {'carrito': carrito})
