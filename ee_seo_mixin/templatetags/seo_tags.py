from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def override_title(seo_object, default):
    title = getattr(seo_object, 'title_override', None)
    return title if title else default


@register.simple_tag
def override_description(seo_object, default):
    description = getattr(seo_object, 'meta_description_override', None)
    return description if description else default


@register.simple_tag
def block_indexing(seo_object, default):
    if hasattr(seo_object, 'block_indexing'):
        block = seo_object.block_indexing
    else:
        block = default
    if block:
        return mark_safe('<meta name="robots" content="noindex"/>')
    else:
        return ''
