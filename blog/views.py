from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import (
    ArchiveIndexView, CreateView, DetailView,
    MonthArchiveView, View, YearArchiveView)

from core.utils import UpdateView

from .forms import PostForm
from .models import Post
from .utils import PostGetMixin


class PostArchiveMonth(MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'


class PostArchiveYear(YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True


class PostCreate(CreateView):
    form_class = PostForm
    model = Post


class PostDelete(View):

    def get(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug)
        return render(
            request,
            'blog/post_confirm_delete.html',
            {'post': post})

    def post(self, request, year, month, slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug)
        post.delete()
        return redirect('blog_post_list')


class PostDetail(PostGetMixin, DetailView):
    model = Post


class PostList(ArchiveIndexView):
    allow_empty = True
    allow_future = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
