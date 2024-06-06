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
def products_by_category(products: list, category: CategoryModel) -> list:
    logger.info(f"products: {products} | category: {category}")
    products_by_category = [product for product in products if product.category.name == category.name]
    logger.info(f"products by category: {products_by_category}")
    return products_by_category
    

@register.filter
def format_number(number: Decimal) -> str:
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    formated_number = locale.format_string("%.2f", number, grouping=True)
    logger.info(f"original number: {number} | formatted number: {formated_number}")
    return formated_number
    

@register.filter
def image_or_default(image: ImageFieldFile) -> str:
    if image:
        url = image.url
    else:
        url = static("images/default-no-image.png")
    logger.info(f"url/path: {url}")
    return url
