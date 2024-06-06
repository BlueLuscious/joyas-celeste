import locale
from django import template

register = template.Library()


@register.filter
def products_in_category(products, category):
    if isinstance(products, dict):
        return products.get(category, [])
    else:
        return [product for product in products if product.category.name == category.name]
    

@register.filter
def format_number(value):
    locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
    return locale.format_string("%.2f", value, grouping=True)
