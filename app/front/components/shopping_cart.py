import logging
from django.contrib import messages
from django.db.models import QuerySet
from django_unicorn.components import UnicornView
from client.models.client_model import ClientModel
from cart.models.cart_item_model import CartItemModel
from cart.models.cart_model import CartModel
from cart.services.models.cart_item_service import CartItemService
from product.models.product_model import ProductModel

logger = logging.getLogger(__name__)


class ShoppingCartView(UnicornView):
    
    """ 
    Unicorn Component for Shopping Cart. 

    **Bound Properties**:
        **cart_items (list[CartItemModel])**: List of cart items.
        **total_amount (float)**: Total amount to pay.
    """

    cart_items: QuerySet[CartItemModel] = CartItemModel.objects.none()
    total_amount: float = 0.0

    def __init__(self, *args, **kwargs) -> None:

        """ ShoppingCartView Initializer. """

        super().__init__(*args, **kwargs)
        self.user: ClientModel = self.request.user
        self.cart_model = CartModel.objects.filter(user=self.request.user).last()
        self.update_cart_items()
        self.update_total_amount()


    def after_action(self):

        """
        Update `Bound Properties` and call JS methods.

        **Actions**:
            - Update `cart_items` reactively.
            - Update `total_amount` reactively.

        **JS Methods**:
            updateCartCounter: Update `cart_items_count` reactively. (ShoppingCartCounterView)
            displayMessages: Show `message_list` reactively. (DjangoMessagesView)
        """

        self.update_cart_items()
        self.update_total_amount()
        self.call("updateCartCounter")
        self.call("displayMessages")


    def add_to_cart(self, product: ProductModel, size: int, quantity: int = 1) -> None:

        """ 
        Add an item to cart reactively.
        
        Args:
            product (ProductModel): Product Instance.
            size (int): Product size.
            quantity (int): Quantity to increase, default 1.
        """

        key = f"{str(product.uuid)}_{size}"
        if not self.cart_items.filter(cart=self.cart_model, key=key).exists():
            cart_item = CartItemService(self.cart_model, product).create_cart_item(key, size, quantity)
            messages.success(self.request, "Producto agregado al carrito")
            logger.info(f"Add item to cart: {cart_item}")
            self.after_action()
        else:
            cart_item = self.cart_items.get(cart=self.cart_model, key=key)
            if cart_item.quantity < cart_item.stock:
                self.increment_quantity(key)
                messages.success(self.request, "Producto actualizado en el carrito")
            else:
                messages.info(self.request, "Cantidad insuficiente")
                logger.info(f"No more stock: {cart_item}")
                self.after_action()


    def remove_from_cart(self, key: str) -> None:

        """ 
        Remove an item from cart reactively.
        
        Args:
            key (str): Unique Identifier.
        """
                
        cart_item = self.cart_items.get(cart=self.cart_model, key=key)
        cart_item.delete()
        messages.success(self.request, "Producto removido del carrito")
        logger.info(f"Remove item from cart: {cart_item}")
        self.after_action()


    def increment_quantity(self, key: str, quantity: int = 1) -> None:

        """ 
        Increases the quantity of a cart item by one reactively.
        
        Args:
            key (str): Unique Identifier.
            quantity (int): Quantity to increase, default 1.
        """
                
        cart_item = self.cart_items.get(cart=self.cart_model, key=key)
        if cart_item.quantity < cart_item.stock:
            cart_item.quantity += quantity
            cart_item.price = cart_item.product.price * cart_item.quantity
        cart_item.save()
        logger.info(f"Increment quantity | Cart item: {cart_item}")
        self.after_action()


    def decrement_quantity(self, key: str, quantity: int = 1) -> None:

        """ 
        Decreases the quantity of a cart item by one reactively.
        
        Args:
            key (str): Unique Identifier.
            quantity (int): Quantity to decrease, default 1.
        """

        cart_item = self.cart_items.get(cart=self.cart_model, key=key)
        if cart_item.quantity > 1:
            cart_item.quantity -= quantity
            cart_item.price = cart_item.product.price * cart_item.quantity
        cart_item.save()
        logger.info(f"Decrement quantity | Cart item: {cart_item}")
        self.after_action()
        

    def clear_cart(self) -> None:

        """ Clear entire `cart_items` reactively. """

        self.cart_model.items.all().delete()
        self.after_action()


    def update_cart_items(self) -> None:
        
        """ Update `cart_items` reactively. """

        if self.user.is_authenticated and self.cart_model:
            self.cart_items = self.cart_model.items.all()
        logger.info(f"Update cart items: {self.cart_items}")


    def update_total_amount(self) -> None:

        """ Update `total_amount` reactively. """

        if self.cart_items:
            self.total_amount = self.cart_model.total_price()
        logger.info(f"Update total amount: {self.total_amount}")
        