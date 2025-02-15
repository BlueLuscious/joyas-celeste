import logging
from django_unicorn.components import UnicornView
from cart.models.cart_item_model import CartItemModel

logger = logging.getLogger(__name__)


class ShoppingCartCounterView(UnicornView):

    """
    Unicorn Component for Shopping Cart Counter. 

    **Bound Properties**:
        **cart_items_count (int)**: Number of items in cart.
    """

    cart_items_count: int = 0

    def __init__(self, *args, **kwargs) -> None:

        """ ShoppingCartCounterView Initializer. """

        super().__init__(*args, **kwargs)
        self.update_cart_counter()


    def update_cart_counter(self) -> None:

        """ Update `cart_items_count` reactively. """

        if self.request.user.is_authenticated:
            self.cart_items_count = CartItemModel.objects.filter(user=self.request.user).count()
        logger.info(f"Quantity of items in cart: {self.cart_items_count}")
            