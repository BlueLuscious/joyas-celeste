from django_unicorn.components import UnicornView
from front.models.cart_item_model import CartItemModel


class ShoppingCartCounterView(UnicornView):
    cart_items_count: CartItemModel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_cart_counter()

    def update_cart_counter(self):
        self.cart_items_count = CartItemModel.objects.count()
