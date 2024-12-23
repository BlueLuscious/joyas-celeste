import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("pages/components-index/category-card.html")
def index_category_card(url: str, category_name: str) -> dict:

    """ 
    Create index category card.

    Args:
        url (str): Redirect url.
        category_name (str): Category name.

    Returns:
        dict: A dictionary with Args.
    """

    data = dict(url=url, category_name=category_name)
    logger.info(f"Category card data: {data}")
    return data
