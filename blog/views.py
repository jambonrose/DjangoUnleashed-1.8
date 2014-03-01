from django.shortcuts import render

from .models import Post


def post_list(request):
    return render(
        request,
        'blog/post_list.html',
        {'post_list': Post.objects.all()})
