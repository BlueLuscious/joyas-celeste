import logging
from django_unicorn.components import UnicornView
from cart.models.cart_model import CartModel

logger = logging.getLogger(__name__)


class ShoppingCartCounterView(UnicornView):

    """
    Unicorn Component for Shopping Cart Counter. 

    **Bound Properties**:
        **cart_items_count (int)**: Number of items in cart.
    """

    cart_items_count: int = 0

    def mount(self) -> None:

        """ ShoppingCartCounterView First Creation. """

        if self.request.user.is_authenticated:
            self.cart_model = CartModel.objects.filter(user=self.request.user).last()
        self.update_cart_counter()


    def update_cart_counter(self) -> None:

        """ Update `cart_items_count` reactively. """

        if self.request.user.is_authenticated and self.cart_model:
            self.cart_items_count = self.cart_model.items.count()
        logger.info(f"Quantity of items in cart: {self.cart_items_count}")
        