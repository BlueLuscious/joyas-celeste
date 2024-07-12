import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("icons/arrow-down.html")
def arrow_icon(tailwind_rotate: str = "") -> dict:
    logger.info(f"rotation: {tailwind_rotate}")
    context = {
        "rotate": tailwind_rotate,
    }
    logger.info(f"tailwind class: {context}")

    return context
