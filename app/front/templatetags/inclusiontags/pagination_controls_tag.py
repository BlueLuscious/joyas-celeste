import logging
from django import template
from front.utils.context import Context

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("pages/components/pagination-controls.html")
def pagination_controls(page_data: dict, page_numbers: list) -> dict:
    context = Context(
        page_data=page_data,
        page_numbers=page_numbers,
    )
    logger.info(f"Pagination controls context: {context}")
    return context.as_dict
