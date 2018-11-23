from django import template
from num2words import num2words

register = template.Library()

@register.filter
def towords(value):        
    return "Rupees %s" % num2words(value)