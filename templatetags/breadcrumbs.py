from django import template

register = template.Library()

@register.inclusion_tag('breadcrumbs.html')
def render_breadcrumbs(breadcrumbs):
    return {'breadcrumbs': breadcrumbs}
