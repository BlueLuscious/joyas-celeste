import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("pages/components/pagination-controls.html")
def pagination_controls(page_data: dict, page_numbers: list) -> dict:

    """ 
    Render pagination controls data.

    Args:
        page_data (dict): Page data.
        page_numbers (str): Pagination controls range.

    Returns:
        dict: A dictionary with Args.
    """
    
    data = dict(page_data=page_data, page_numbers=page_numbers)
    logger.info(f"Pagination controls context: {data}")
    return data
