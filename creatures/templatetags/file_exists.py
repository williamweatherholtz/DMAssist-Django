import re

from django import template
from django.core.files.storage import default_storage
register = template.Library()

@register.filter
def file_exists(path):
    return default_storage.exists(path)
