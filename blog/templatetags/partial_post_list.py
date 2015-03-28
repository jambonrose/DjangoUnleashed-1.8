from django import template

# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/

register = template.Library()


@register.inclusion_tag(
    'blog/includes/partial_post_list.html',
    takes_context=True)
def format_post_list(context, detail_object):
    request = context.get('request')
    future_perms = request.user.has_perm(
        'blog.view_future_post')
    if future_perms:
        post_list = detail_object.blog_posts.all()
    else:
        post_list = detail_object.published_posts
    return {
        'post_list': post_list,
    }
