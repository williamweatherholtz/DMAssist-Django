import re

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def remove_newline(str):
    return re.sub('[\n]', '', str)
