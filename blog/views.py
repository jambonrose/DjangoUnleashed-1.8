from django.shortcuts import (
    get_object_or_404, render)
from django.views.generic import View

from .models import Post


def post_detail(request, year, month,
                slug, parent_template=None):
    post = get_object_or_404(
        Post,
        pub_date__year=year,
        pub_date__month=month,
        slug=slug)
    return render(
        request,
        'blog/post_detail.html',
        {'post': post,
         'parent_template': parent_template})


class PostList(View):

    def get(self, request, parent_template=None):
        return render(
            request,
            'blog/post_list.html',
            {'post_list': Post.objects.all(),
             'parent_template': parent_template})
