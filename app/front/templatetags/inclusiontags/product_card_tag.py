import logging
from django import template
from django.http import HttpRequest
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("pages/components/product-card.html")
def product_card(request: HttpRequest, product: ProductModel, dollar_blue: int) -> dict:
    logger.info(f"product: {product} | dollar blue: {dollar_blue}")
    context = {
        "request": request,
        "product": product,
        "dollar_blue": dollar_blue,
    }
    logger.info(f"product card context: {context}")
    return context
