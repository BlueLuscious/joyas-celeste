from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import QuerySet
from typing import TYPE_CHECKING
from uuid import uuid4
if TYPE_CHECKING:
    from front.models.cart_item_model import CartItemModel


class ClientModel(AbstractUser):

    """
    Client Model.

    Fields:
        username (str): Username.
        first_name (str): First name.
        last_name (str): Last name.
        email (str): Email.
        is_staff (bool): Is staff User.
        is_active (bool) Is active User.
        date_joined (DateTime): Joined date.
        uuid (UUID): Universal Unique Identifier.
        created_at (DateTime): Creation date.
        updated_at (DateTime): Update date.

    Related Fields:
        cart_item_user (Queryset[CartItemModel]): CartItemModel Queryset.
    """

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    cart_item_user: "QuerySet[CartItemModel]"


    def __str__(self) -> str:

        """
        Overwrite __str__ method.
        
        Returns:
            str: Client username.
        """

        return self.username
    