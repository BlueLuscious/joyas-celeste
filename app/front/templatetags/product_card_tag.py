import logging
from django import template
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("pages/components/product-card.html")
def product_card(products: ProductModel, dollar_blue: int, category: str = None) -> dict:
    logger.info(f"products: {products} | dollar blue: {dollar_blue} | category: {category}")
    context = {
        "products": products,
        "category": category,
        "dollar_blue": dollar_blue,
    }
    logger.info(f"product card context: {context}")

    return context
