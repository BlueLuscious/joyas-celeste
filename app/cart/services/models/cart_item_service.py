import logging
from cart.models.cart_item_model import CartItemModel
from cart.models.cart_model import CartModel
from product.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class CartItemService:

    """ Services for CartItemModel. """

    def __init__(self, cart: CartModel, product: ProductModel) -> None:

        """
        CartItemService Initializer.

        Args:
            cart (CartModel): Cart Instance.
            product (ProductModel): Product Instance.
        """

        self.cart = cart
        self.product = product
        

    def create_cart_item(self, key: str, size: int, quantity: int = 1) -> CartItemModel:

        """
        Create a cart item instance.

        Args:
            key (str): Unique Identifier.
            size (int): Product size.
            quantity (int): Quantity to increase, default 1.

        Returns:
            CartItemModel: CartItem Instance.
        """

        cart_item = CartItemModel.objects.create(
            key=key,
            cart=self.cart,
            product=self.product,
            price=self.product.price,
            size=size,
            stock=self.product.variations.filter(measure__size=size).first().stock,
            quantity=quantity
        )
        
        logger.info(f"Cart item created: {cart_item}")
        return cart_item
    