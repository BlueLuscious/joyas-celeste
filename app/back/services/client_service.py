import logging
from back.exceptions.sign_up_exception import SignUpError
from back.models.client_model import ClientModel

logger = logging.getLogger(__name__)


class ClientService:

    @staticmethod
    def create_client(data: dict) -> ClientModel:

        """
        Create a ClientModel instance.

        Args:
            data (dict): Validated form data.

        Returns:
            ClientModel: ClientModel instance.
        """

        try:
            user = ClientModel.objects.create_user(**data)
            logger.info(f"User {user.username} was created")
            return user
        except Exception as e:
            raise SignUpError("Ocurrió un error inesperado") from e # Cambiar Exception
        