import logging
import mercadopago
from django.db.models import QuerySet
from app.settings import MP_PUBLIC_KEY, MP_ACCESS_TOKEN
from front.models.cart_item_model import CartItemModel
from front.templatetags.filters.product_filter import convert_price_to_ARS

logger = logging.getLogger(__name__)


class MercadoPagoService():

    """ Service for MercadoPago. """

    def __init__(self) -> None:

        """ MercadoPagoService Initializer. """

        self.public_key: str = MP_PUBLIC_KEY
        self.access_token: str = MP_ACCESS_TOKEN


    # Checkout Pro Integration
    def create_preference(self, cart_items: QuerySet[CartItemModel], dollar: float) -> dict:

        """
        Create payment for MercadoPago.
        
        Args:
            cart_items (QuerySet[CartItemModel]): Cart items.
            dollar (float): Dollar quote.

        Returns:
            dict: Preference data.
        """

        sdk = mercadopago.SDK(self.access_token)

        preference_data = {
            "items": [
                {
                    "id": str(cart_item.product.uuid),
                    "category_id": cart_item.product.category.name,
                    "currency_id": "ARS",
                    "description": cart_item.product.description,
                    "title": cart_item.product.name,
                    "quantity": cart_item.quantity,
                    "unit_price": float(convert_price_to_ARS(cart_item.price, dollar)),
                }
                for cart_item in cart_items
            ],
        }

        preference_response = sdk.preference().create(preference_data)
        logger.info(f"preference response: {preference_response}")

        preference = preference_response["response"]
        logger.info(f"preference: {preference}")

        return preference
