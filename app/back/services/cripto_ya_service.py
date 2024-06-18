import logging
import requests
from app.settings import CRIPTO_YA_BASE_URL

logger = logging.getLogger(__name__)


class CriptoYaService():

    @staticmethod
    def get_dollar_quotes() -> dict:

        """
        Get dollar quotes from CriptoYa Api.

        Returns:
            dict: Dictionary containing different dollar quotes and response status code.
        """

        url = f"{CRIPTO_YA_BASE_URL}/api/dolar"
        logger.info(f"url: {url}")

        response = requests.get(url)
        logger.info(f"response status: {response.status_code}")
        logger.info(f"response data: {response.json()}")

        return {
            "data": response.json(),
            "status": response.status_code,
        }
