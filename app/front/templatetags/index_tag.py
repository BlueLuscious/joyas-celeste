import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("pages/components-index/category-card.html")
def category_card(url: str, category_name: str) -> dict:
    logger.info(f"url: {url} | category: {category_name}")
    context = {
        "url": url,
        "category_name": category_name,
    }
    logger.info(f"category card context: {context}")

    return context
