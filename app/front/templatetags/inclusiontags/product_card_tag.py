import logging
from django import template
from django.http import HttpRequest
from front.models.product_model import ProductModel

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("pages/components/product-card.html")
def product_card(request: HttpRequest, product: ProductModel, dollar_blue: float) -> dict:

    """ 
    Create info content in footer.

    Args:
        request (HttpRequest): Request.
        product (ProductModel): ProductModel Instance.
        dollar_blue (float): Dollar quote.

    Returns:
        dict: A dictionary with Args.
    """

    context = dict(request=request, product=product, dollar_blue=dollar_blue)
    logger.info(f"product card context: {context}")
    return context
