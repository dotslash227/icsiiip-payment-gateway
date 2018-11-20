from django import template
from num2words import num2words

register = template.Library()

@register.filter
def towords(value):    
    
    print (num2words(value, lang="en_IN"))
    return "Rupees %s" % num2words(value)