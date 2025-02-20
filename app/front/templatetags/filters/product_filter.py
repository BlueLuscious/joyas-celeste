import locale
import logging
from decimal import Decimal
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.filter
def convert_price_to_ARS(price: Decimal, dollar: float) -> Decimal:

    """
    Convert price in USD to ARS.
    
    Args:
        price (Decimal): Product price.
        dollar (float): Dollar quote.

    Returns:
        Decimal: Converted price.
    """

    logger.info(f"price: {price} | dollar: {dollar}")
    try:
        converted_price = Decimal(price) * dollar
        logger.info(f"converted price: {converted_price}")
        return converted_price
    except TypeError:
        logger.info(f"convertion failed, load original price")
        return price


@register.filter
def format_number_AR(number: Decimal) -> str:

    """ 
    Format number to string in AR locale.
    
    Args:
        number (Decimal): Product price.

    Returns:
        str: Formatted number.
    """

    locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')
    formatted_number = locale.format_string("%.2f", number, grouping=True)
    logger.info(f"original number: {number} | formatted number: {formatted_number}")
    return formatted_number
    