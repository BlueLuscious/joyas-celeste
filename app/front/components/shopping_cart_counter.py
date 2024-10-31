from django_unicorn.components import UnicornView
from front.models.cart_item_model import CartItemModel


class ShoppingCartCounterView(UnicornView):
    cart_items_count: int = 0

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.update_cart_counter()


    def update_cart_counter(self) -> None:
        if self.request.user.is_authenticated:
            self.cart_items_count = CartItemModel.objects.filter(user=self.request.user).count()
            