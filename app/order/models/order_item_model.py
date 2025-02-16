# from typing import TYPE_CHECKING
from uuid import uuid4
from django.db import models
from cart.models.cart_item_model import CartItemModel
from order.models.order_model import OrderModel
from product.models.product_model import ProductModel


class OrderItemModel(models.Model):

    """
    OrderItem Model.

    Fields:
        uuid (UUID): Universal Unique Identifier.
        order (OrderModel): OrderModel Instance.
        product (ProductModel): Product Instance.
        price (Decimal): Cart item price.
        size (str): Product size.
        quantity (int): Cart item quantity
        created_at (datetime): Creation date.
        updated_at (datetime): Update date.
    """

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING) # TODO: Think what to do when it's on_delete.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=128)
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
    
    
    def create_order_item(cls, cart_item: CartItemModel, order: OrderModel) -> "OrderItemModel":
        
        """
        Create a OrderItemModel.

        Args:
            cart_item (CartItemModel): CartItemModel Instance.
            order (OrderModel): OrderModel Instance.

        Returns:
            OrderItemKModel: OrderItemModel Instance.
        """

        return cls(
            order=order,
            product=cart_item.product,
            price=cart_item.price,
            size=cart_item.size,
            quantity=cart_item.quantity
        )
    