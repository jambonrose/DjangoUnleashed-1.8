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


@register.tag(name="get_latest_posts")
def do_latest_posts(parser, token):
    try:
        tag_name, number_of_posts_str = (
            token.split_contents())
    except ValueError:
        raise TemplateSyntaxError(
            "get_latest_posts takes 1 argument: "
            "number of posts to get")
    try:
        number_of_posts = int(number_of_posts_str)
    except ValueError:
        raise TemplateSyntaxError(
            "tag '{tag_display}' sole argument "
            "must be an integer".format(
                tag_display=tag_name))
    return LatestPostsNode(number_of_posts)


class LatestPostsNode(Node):

    def __init__(self, number_of_posts):
        self.num = number_of_posts

    def render(self, context):
        context['latest_posts_list'] = (
            Post.objects.published()[:self.num])
        return str()
