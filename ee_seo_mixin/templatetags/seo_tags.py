from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def override_title(seo_object):
    return getattr(seo_object, 'title_override', seo_object)


@register.simple_tag
def override_description(seo_object):
    return getattr(seo_object, 'meta_description_override', seo_object)


@register.simple_tag
def block_indexing(seo_object):
    if seo_object or getattr(seo_object, 'block_indexing', False):
        return mark_safe('<meta name="robots" content="noindex"/>')
    else:
        return ''
