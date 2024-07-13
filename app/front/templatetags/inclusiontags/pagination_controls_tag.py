import logging
from django import template
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("pages/components/pagination-controls.html")
def pagination_controls(products: ProductModel, page_numbers: list) -> dict:
    logger.info(f"products: {products} | page numbers: {page_numbers}")
    context = {
        "products": products,
        "page_numbers": page_numbers,
    }
    logger.info(f"pagination controls context: {context}")

    return context
