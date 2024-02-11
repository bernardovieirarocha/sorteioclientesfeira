from django import template

register = template.Library()

@register.filter
def my_filter(data):
    return data + 'Alterado por filter'

@register.filter
def arredonda(value,casas):
    return round(value,casas)