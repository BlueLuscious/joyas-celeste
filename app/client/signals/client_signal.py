import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from client.models.client_model import ClientModel
from cart.models.cart_model import CartModel

logger = logging.getLogger(__name__)


@receiver(post_save, sender=ClientModel)
def create_cart_for_new_client(sender, instance: ClientModel, created: bool, **kwargs) -> None:

    """ Create a Cart when a new Client is created. """

    if created and not instance.is_superuser:
        cart_model = CartModel.objects.create(user=instance)
        if cart_model:
            logger.info(f"Cart created for user: {instance}")
        else:
            logger.info(f"Cart not created for user: {instance}")
            