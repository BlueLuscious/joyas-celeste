import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("icons/whatsapp.html")
def whatsapp_icon(tailwind_class: str = "") -> dict:
    context = {
        "tailwind_class": tailwind_class,
    }
    logger.info(f"tailwind class: {context}")

    return context
