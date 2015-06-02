from io import StringIO

from django import template

# https://docs.djangoproject.com/en/1.8/howto/custom-template-tags/

register = template.Library()


@register.simple_tag
def format_post_list(post_list):
    indent = '  '
    output = StringIO()
    output.write('<ul>\n')
    for post in post_list:
        output.write(
            '{}<li><a href="{}">\n'.format(
                indent, post.get_absolute_url()))
        output.write('{}{}\n'.format(
            indent * 2, post.title.title()))
        output.write('{}</a></li>\n'.format(
            indent))
    output.write('</ul>\n')
    return output.getvalue()
