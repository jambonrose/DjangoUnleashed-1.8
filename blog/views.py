from django.shortcuts import (
    get_object_or_404, render)

from .models import Post


def post_detail(request, year, month, slug):
    post = get_object_or_404(
        Post,
        pub_date__year=year,
        pub_date__month=month,
        slug=slug)
    return render(
        request,
        'blog/post_detail.html',
        {'post': post})


def post_list(request):
    return render(
        request,
        'blog/post_list.html',
        {'post_list': Post.objects.all()})
