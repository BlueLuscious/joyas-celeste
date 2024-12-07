from back.models.client_model import ClientModel
from front.models.cart_item_model import CartItemModel
from front.models.product_model import ProductModel


class CartItemService:

    """ Services for CartItemModel. """

    def __init__(self, user: ClientModel, product: ProductModel) -> None:

        """
        CartItemService Initializer.

        Args:
            user (ClientModel): Client Instance.
            product (ProductModel): Product Instance.
        """

        self.user = user
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
            user=self.user,
            product=self.product,
            price=self.product.price,
            size=size,
            stock=self.product.variations.filter(measure__size=size).first().stock,
            quantity=quantity
        )
        return cart_item
    