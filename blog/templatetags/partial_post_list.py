from django import template

# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/

register = template.Library()


@register.inclusion_tag(
    'blog/includes/partial_post_list.html')
def format_post_list(post_list):
    return {
        'post_list': post_list,
    }
