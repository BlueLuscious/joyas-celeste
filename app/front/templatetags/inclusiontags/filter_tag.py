import logging
from django import template
from django.db.models import QuerySet
from front.utils.context import Context

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("unicorn/products-components/filters/select-filter.html")
def select_filter(select_id: str, selected_filter: str, unicorn_method: str, filter_name: str, criterias: QuerySet) -> dict:
    context = Context(
        select_id=select_id,
        selected_filter=selected_filter,
        unicorn_method=unicorn_method,
        filter_name=filter_name,
        criterias=criterias,
    )
    logger.info(f"select filter context: {context.as_dict}")
    return context.as_dict
