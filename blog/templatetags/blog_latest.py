from django.template import (
    Library, Node, TemplateSyntaxError)

from ..models import Post

# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/
register = Library()


@register.tag(name="get_latest_post")
def do_latest_post(parser, token):
    return LatestPostNode()


class LatestPostNode(Node):

    def render(self, context):
        context['latest_post'] = (
            Post.objects.published().latest())
        return str()
