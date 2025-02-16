from typing import TYPE_CHECKING
from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models
if TYPE_CHECKING:
    from cart.models.cart_model import CartModel


class ClientModel(AbstractUser):

    """
    Client Model.

    Abstract User Fields:
        username (str): Username.
        first_name (str): First name.
        last_name (str): Last name.
        email (str): Email.
        is_staff (bool): Is staff User.
        is_active (bool) Is active User.
        date_joined (datetime): Joined date.
    
    Fields:
        uuid (UUID): Universal Unique Identifier.
        created_at (datetime): Creation date.
        updated_at (datetime): Update date.

    Related Fields:
        cart (CartModel): CartModel Instance.
    """

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    cart: "CartModel"


    def __str__(self) -> str:

        """
        Overwrite __str__ method.
        
        Returns:
            str: Client username.
        """

        return self.username
    