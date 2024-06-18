import locale
import logging
from decimal import Decimal
from django import template
from django.db.models.fields.files import ImageFieldFile
from django.templatetags.static import static
from front.models.category_model import CategoryModel

logger = logging.getLogger(__name__)
register = template.Library()


@register.filter
def convert_price_to_ARS(price: Decimal, dollar: int) -> Decimal:
    logger.info(f"price: {price} | dollar: {dollar}")
    try:
        converted_price = price * dollar
        logger.info(f"converted price: {converted_price}")
        return converted_price
    except TypeError:
        logger.info(f"convertion failed, load original price")
        return price


@register.filter
def format_number_AR(number: Decimal) -> str:
    locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')
    formatted_number = locale.format_string("%.2f", number, grouping=True)
    logger.info(f"original number: {number} | formatted number: {formatted_number}")
    return formatted_number
    

@register.filter
def image_or_default(image: ImageFieldFile) -> str:
    if image:
        url = image.url
    else:
        url = static("images/default-no-image.png")
    logger.info(f"url/path: {url}")
    return url


@register.filter
def products_by_category(products: list, category: CategoryModel) -> list:
    logger.info(f"products: {products} | category: {category}")
    products_by_category = [product for product in products if product.category.name == category.name]
    logger.info(f"products by category: {products_by_category}")
    return products_by_category
