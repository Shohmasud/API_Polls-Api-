from django import template
register = template.Library()

@register.filter(name='array_to_string')
def array_to_string(array):
    return ''.join(array)


