import logging
from django.contrib import messages
from django.db.models import QuerySet
from django_unicorn.components import UnicornView
from cart.models.cart_item_model import CartItemModel
from cart.models.cart_model import CartModel
from cart.services.models.cart_item_service import CartItemService
from client.models.client_model import ClientModel
from product.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class ShoppingCartView(UnicornView):
    
    """ 
    Unicorn Component for Shopping Cart. 

    **Bound Properties**:
        **is_cart_open (bool)**: Open cart or keep it close.
        **cart (CartModel)**: Cart Instance.
        **cart_items (QuerySet[CartItemModel])**: Cart items queryset.
    """

    is_cart_open: bool = False
    cart: CartModel = None
    cart_items: QuerySet[CartItemModel] = CartItemModel.objects.none()
    user: ClientModel = None

    def mount(self) -> None:
        self.user = self.request.user if self.request.user.is_authenticated else None
        if self.user:
            self.user = ClientModel.objects.get(pk=self.user.pk)


    def hydrate(self) -> None:
        self.set_cart()
        self.set_cart_items()


    def display_cart(self, is_open: bool) -> None:

        """
        Display cart sidebar reactively.

        Args:
            is_open (bool): If `True` open cart else keep it close.
        """

        self.is_cart_open = is_open


    def set_cart(self) -> None:

        """ Set `cart` reactively. """

        self.cart = CartModel.objects.filter(user=self.user).last() if self.user.is_authenticated else None
        logger.info(f"Set cart: {self.cart}")


    def set_cart_items(self) -> None:
        
        """ Set `cart_items` reactively. """

        self.cart_items = self.cart.items.all() if self.cart else CartItemModel.objects.none()
        logger.info(f"Set cart items: {self.cart_items}")


    def add_to_cart(self, product: ProductModel, size: int, quantity: int = 1) -> None:

        """ 
        Add an item to cart reactively.
        
        Args:
            product (ProductModel): Product Instance.
            size (int): Product size.
            quantity (int): Quantity to increase, default 1.
        """

        key = f"{str(product.uuid)}_{size}"
        if not CartItemModel.objects.filter(cart=self.cart, key=key).exists():
            cart_item = CartItemService(self.cart, product).create_cart_item(key, size, quantity)
            logger.info(f"Add item to cart: {cart_item}")
            self.call("addMessage", messages.SUCCESS, "Producto agregado al carrito")
        else:
            cart_item = CartItemModel.objects.get(cart=self.cart, key=key)
            if cart_item.quantity < cart_item.stock:
                self.increment_quantity(key)
                self.call("addMessage", messages.SUCCESS, "Producto actualizado al carrito")
            else:
                logger.info(f"No more stock: {cart_item}")
                self.call("addMessage", messages.INFO, "Cantidad insuficiente")


    def remove_from_cart(self, key: str) -> None:

        """ 
        Remove an item from cart reactively.
        
        Args:
            key (str): Unique Identifier.
        """

        cart_item = CartItemModel.objects.get(cart=self.cart, key=key)
        cart_item.delete()
        logger.info(f"Remove item from cart: {cart_item}")
        self.call("addMessage", messages.SUCCESS, "Producto removido del carrito")


    def increment_quantity(self, key: str, quantity: int = 1) -> None:

        """ 
        Increases the quantity of a cart item by one reactively.
        
        Args:
            key (str): Unique Identifier.
            quantity (int): Quantity to increase, default 1.
        """
        
        cart_item = CartItemModel.objects.get(cart=self.cart, key=key)
        if cart_item.quantity < cart_item.stock:
            cart_item.quantity += quantity
            cart_item.price = cart_item.product.price * cart_item.quantity
            cart_item.save()
            self.set_cart_items()
        logger.info(f"Increment quantity | Cart item: {cart_item}")


    def decrement_quantity(self, key: str, quantity: int = 1) -> None:

        """ 
        Decreases the quantity of a cart item by one reactively.
        
        Args:
            key (str): Unique Identifier.
            quantity (int): Quantity to decrease, default 1.
        """

        cart_item = CartItemModel.objects.get(cart=self.cart, key=key)
        if cart_item.quantity > 1:
            cart_item.quantity -= quantity
            cart_item.price = cart_item.product.price * cart_item.quantity
            cart_item.save()
            self.set_cart_items()
        logger.info(f"Decrement quantity | Cart item: {cart_item}")
        

    def clear_cart(self) -> None:

        """ Clear entire `cart_items` reactively. """

        cart_items = CartItemModel.objects.filter(self.cart).delete()
        self.call("addMessage", messages.SUCCESS, "Carrito limpiado exitosamente")
