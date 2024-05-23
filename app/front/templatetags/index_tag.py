from django import template

register = template.Library()


@register.inclusion_tag("pages/t-index/category-card.html")
def category_card(url, category_name):
    context = {
        "url": url,
        "category_name": category_name,
    }
    return context
