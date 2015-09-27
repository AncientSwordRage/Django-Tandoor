from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def in_category(things, category):
    return things.filter(categoryType=category)

@register.simple_tag
def multiglyph(factor, icon_name):
    multi_glyph = '<i class="fa fa-{icon_name}"></i>'.format(icon_name=icon_name)
    if factor is True:
    	return multi_glyph
    elif factor is None:
    	return ''
    return mark_safe(multi_glyph * factor)

import re

@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return 'active'
    return ''