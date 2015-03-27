from django import template
from django.template.defaultfilters import (
    stringfilter)

# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/

register = template.Library()

@register.filter('obfuscate', is_safe=False)
@stringfilter
def obfuscate_email(value):
    return (value
            .replace('@', ' at ')
            .replace('.',' dot '))
