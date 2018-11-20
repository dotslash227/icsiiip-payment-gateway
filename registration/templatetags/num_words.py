from django import template
import num2words

register = template.Library()

@register.filter
def towords(value):
    return num2words(value, lang="en")