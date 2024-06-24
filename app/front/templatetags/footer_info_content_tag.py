import logging
from django import template
from django.template import Template, Context

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("pages/components/footer-info-content.html", takes_context=True)
def footer_info_content(context, id_: str = "", tag_name: str = "", icon_template: str = "", content: str = "") -> dict:

    if icon_template.endswith(".html"):
        icon_html = context.template.engine.get_template(icon_template).render(context)
    else:
        template_string = f"{{% load {tag_name} %}} {{% {icon_template} %}}"
        icon_html = Template(template_string).render(Context(context.flatten()))

    context_ = {
        "id": id_,
        "icon_html": icon_html,
        "tag_name": tag_name,
        "content": content,
    }
    logger.info(f"footer info card context: {context_}")

    return context_
