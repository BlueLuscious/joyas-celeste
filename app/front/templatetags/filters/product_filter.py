import logging
from babel import numbers
from decimal import Decimal
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.filter
def convert_price_to_ARS(price: Decimal, dollar: int) -> Decimal:

    """
    Convert price in USD to ARS.
    
    Args:
        price (Decimal): Product price.
        dollar (int): Dollar quote.

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

    formatted_number = numbers.format_decimal(number, locale='es_AR', format='#,##0.00')
    logger.info(f"original number: {number} | formatted number: {formatted_number}")
    return formatted_number
    