from django.core.exceptions import \
    ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.template import (
    Library, TemplateSyntaxError)

# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/
register = Library()


@register.inclusion_tag(
    'core/includes/form.html',
    takes_context=True)
def form(context, *args, **kwargs):
    action = (args[0] if len(args) > 0
              else kwargs.get('action'))
    button = (args[1] if len(args) > 1
              else kwargs.get('button'))
    method = (args[2] if len(args) > 2
              else kwargs.get('method'))
    form = context.get('form')
    if action is None:
        raise TemplateSyntaxError(
            "form template tag requires "
            "at least one argument: action, "
            "which is a URL.")
    return {
        'action': action,
        'button': button,
        'form': form,
        'method': method}
