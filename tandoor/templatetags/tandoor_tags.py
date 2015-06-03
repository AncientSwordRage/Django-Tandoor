from django import template
register = template.Library()

@register.filter
def multiglyph(times, string):
    multi_glyph = '<i glyphicon-font glyphicon-{glyph}></i>'.format(glyph=string)
    return multi_glyph * times