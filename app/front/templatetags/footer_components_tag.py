import logging
from django import template
from django.template import Template, Context

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag("components-base/components-footer/footer-info-content.html", takes_context=True)
def footer_info_content(context, id_: str, icon_inclusion: str, content: str) -> dict:

    template_string = f"{{% include {icon_inclusion} %}}"
    icon_html = Template(template_string).render(Context(context.flatten()))

    context_ = {
        "id": id_,
        "icon_html": icon_html,
        "content": content,
    }
    logger.info(f"footer info card context: {context_}")

    return context_
