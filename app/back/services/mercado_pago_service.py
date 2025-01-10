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

        buyer_email = "TESTUSER1196750206"
        buyer_password = "pdwlwZAnin"
        seller_email = "TESTUSER1810854595"
        seller_password = "5RT5mT4AmO"

        mastercard_no = "5031 7557 3453 0604"
        mastercard_code = "123"
        mastercard_expired = "11/25"
        visacard_no = "4509 9535 6623 3704"
        visacard_code = "123"
        visacard_expired = "11/25"


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
