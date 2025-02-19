import logging
import requests
from app.settings import CRIPTO_YA_BASE_URL

logger = logging.getLogger(__name__)


class CriptoYaService:

    """ Service for CriptoYa Api. """

    def __init__(self) -> None:

        """ CriptoYaService Initializer. """
        
        self.base_url = CRIPTO_YA_BASE_URL


    def get_dollar_quotes(self) -> dict:

        """
        Get dollar quotes from CriptoYa Api.

        Returns:
            dict: Dictionary containing different dollar quotes.
        """

        # TODO: Create exceptions.

        url = f"{self.base_url}/api/dolar"
        logger.info(f"url: {url}")

        response = requests.get(url)
        logger.info(f"response status: {response.status_code}")
        logger.info(f"response data: {response.json()}")

        return response.json()
