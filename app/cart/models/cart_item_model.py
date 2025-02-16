from decimal import Decimal
from django.db import models
from cart.models.cart_model import CartModel
from product.models.product_model import ProductModel


class CartItemModel(models.Model):

    """
    Cart Item Model.

    Fields:
        id (int): Identifier, Primary Key.
        key (str): Mixing concatenation product uuid and product size.
        cart (CartModel): CartModel Instance.
        product (ProductModel): Product Instance.
        price (Decimal): Cart item price.
        size (str): Product size.
        stock (int): Product stock.
        quantity (int): Cart item quantity
        created_at (datetime): Creation date.
        updated_at (datetime): Update date.
    """

    id = models.BigAutoField(primary_key=True)
    key = models.CharField(max_length=128)
    cart = models.ForeignKey(
        CartModel, on_delete=models.CASCADE, related_name="items"
    )
    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, related_name="cart_item"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    size = models.CharField(max_length=128)
    stock = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:

        """
        Overwrite __str__ method.
        
        Returns:
            str: Product name.
        """

        return self.product.name


    def total_price(self) -> Decimal:

        """
        Calculate total price of the item (Product price * Item quantity).
        
        Returns:
            Decimal: Total price of the item.
        """

        return self.product.price * self.quantity
    

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["cart", "key"], name="unique_cart_key")
        ]
