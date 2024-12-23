import logging
from back.exceptions.sign_up_exception import SignUpError
from back.models.client_model import ClientModel

logger = logging.getLogger(__name__)


class ClientService:

    """ Service for Client Model. """

    def __init__(self, user: ClientModel = None) -> None:

        """
        ClientService Initializer.

        Args:
            user (ClientModel): ClientModel Instance.
        """

        self.user = user


    def create_client(self, data: dict) -> ClientModel:

        """
        Create a ClientModel instance.

        Args:
            data (dict): Validated form data.

        Returns:
            ClientModel: ClientModel Instance.
        """

        if data:
            user = ClientModel.objects.create_user(**data)
            logger.info(f"User {user.username} was created")
            return user
        else:
            raise SignUpError("Failed to create client. Data is empty")
        