import logging
from django import template
from django.template import Context, Template
from django.template.context import RequestContext

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("components-base/components-footer/footer-info-content.html", takes_context=True)
def footer_info_content(context: RequestContext, id_: str, icon_inclusion: str, content: str) -> dict:

    """ 
    Create info content in footer.

    Args:
        context (RequestContext): Context.
        id_ (str): Element ID.
        icon_inclusion (str): Template to include.
        content (str): Text content.

    Returns:
        dict: A dictionary with Args.
    """

    template_string = f"{{% include {icon_inclusion} %}}"
    icon_html = Template(template_string).render(Context(context.flatten()))

    data = dict(id=id_, icon_html=icon_html, content=content)
    logger.info(f"Footer info card data: {data}")

    return data
