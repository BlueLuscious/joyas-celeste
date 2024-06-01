from django import template

register = template.Library()


@register.filter
def products_in_category(products, category):
    if isinstance(products, dict):
        return products.get(category, [])
    else:
        return [product for product in products if product.category.name == category.name]
