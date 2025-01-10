import logging
from django import template

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("components-base/components-footer/footer-info-content.html")
def footer_info_content(id_: str, content: str, event: str = "", icon_tailwind_class: str = "") -> dict:

    """ 
    Create info content in footer.

    Args:
        id_ (str): Element ID and Icon name.
        content (str): Text content.
        event (str): Method name.
        icon_tailwind_class (str): Icon styles.

    Returns:
        dict: A dictionary with Args.
    """

    data = dict(
        id=id_,
        content=content,
        event=event,
        icon_tailwind_class=icon_tailwind_class,
    )
    logger.info(f"Footer info card data: {data}")
    return data
