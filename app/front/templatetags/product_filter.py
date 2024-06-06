import locale
from decimal import Decimal
from django import template
from django.db.models.fields.files import ImageFieldFile
from django.templatetags.static import static
from front.models.category_model import CategoryModel

register = template.Library()


@register.filter
def products_in_category(products: list, category: CategoryModel) -> list:
    return [product for product in products if product.category.name == category.name]
    

@register.filter
def format_number(value: Decimal) -> str:
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    return locale.format_string("%.2f", value, grouping=True)
    

@register.filter
def image_or_default(image: ImageFieldFile) -> str:
    if image:
        url = image.url
    else:
        url = static("images/default-no-image.png")
    return url
