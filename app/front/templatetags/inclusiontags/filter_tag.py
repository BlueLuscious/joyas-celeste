import logging
from django import template
from django.db.models import QuerySet

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("unicorn/products-components/filters/select-filter.html")
def select_filter(select_id: str, selected_filter: str, unicorn_method: str, filter_name: str, criterias: QuerySet) -> dict:

    """ 
    Create select filter.

    Args:
        select_id (str): Element ID.
        selected_filter (str): Filter type.
        unicorn_method (str): Method to execute.
        filter_name (str): Filter label.
        criterias (QuerySet): Criterias to filter.

    Returns:
        dict: A dictionary with Args.
    """
        
    data = dict(
        select_id=select_id,
        selected_filter=selected_filter,
        unicorn_method=unicorn_method,
        filter_name=filter_name,
        criterias=criterias,
    )
    logger.info(f"Select filter data: {data}")
    return data
