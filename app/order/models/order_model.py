from typing import TYPE_CHECKING
from uuid import uuid4
from django.db import models
from django.db.models import QuerySet
from client.models.client_model import ClientModel
from order.models.choices.status_order_choices import StatusOrderChoices
if TYPE_CHECKING:
    from order.models.order_item_model import OrderItemModel


class OrderModel(models.Model):

    """
    Order Model.

    Fields:
        uuid (UUID): Universal Unique Identifier.
        user (ClientModel): ClientModel Instance.
        status (str): Order status.
        paid (bool): Payment made.
        created_at (datetime): Creation date.
        updated_at (datetime): Update date.

    Related Fields:
        items (QuerySet[OrderItemModel]): OrderItemModel Instances.
    """

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    user = models.ForeignKey(ClientModel, on_delete=models.DO_NOTHING, related_name="orders")
    status = models.CharField(max_length=20, choices=StatusOrderChoices.choices, default=StatusOrderChoices.PENDING)
    paid = models.BooleanField(default=False)
    # TODO: payment_day field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    items: "QuerySet[OrderItemModel]"


    def __str__(self) -> str:
        
        """
        Overwrite __str__ method.
        
        Returns:
            str: Order uuid and related user.
        """
                
        return f"Order: {self.uuid} - {self.user}"
    

    def create_order(cls, user: ClientModel) -> "OrderModel":
        
        """
        Create a OrderModel.

        Args:
            user (ClientModel): ClientModel Instance.

        Returns:
            OrderModel: OrderModel Instance.
        """

        return cls(
            user=user,
        )
    