from typing import TYPE_CHECKING
from uuid import uuid4
from django.db import models
from django.db.models import QuerySet
from client.models.client_model import ClientModel
if TYPE_CHECKING:
    from cart.models.cart_item_model import CartItemModel


class CartModel(models.Model):
    
    """
    Cart Model.
    
    Fields:
        uuid (UUID): Universal Unique Identifier.
        user (ClientModel): ClientModel Instance.
        created_at (UUID): Creation date.
        updated_at (UUID): Update date.

    Related Fields:
        items (QuerySet[CartItemModel]): CartItemModel Instances.
    """
    
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    user = models.OneToOneField(ClientModel, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    items: "QuerySet[CartItemModel]"


    def __str__(self) -> str:

        """
        Overwrite __str__ method.
        
        Returns:
            str: Cart uuid and related user.
        """
        
        return f"Cart: {self.uuid} - {self.user}"


    def total_price(self) -> int:

        """
        Calculate the total amount of the cart.

        Returns:
            int: Total amount of the cart.
        """

        return sum(item.total_price() for item in self.items.all())
    