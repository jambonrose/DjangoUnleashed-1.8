from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ArchiveIndexView, CreateView, DeleteView,
    DetailView, MonthArchiveView, YearArchiveView)

from core.utils import UpdateView
from user.decorators import \
    require_authenticated_permission

from .forms import PostForm
from .models import Post
from .utils import (
    AllowFuturePermissionMixin, DateObjectMixin,
    PostFormValidMixin)


class PostArchiveMonth(
        AllowFuturePermissionMixin,
        MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'


class PostArchiveYear(
        AllowFuturePermissionMixin,
        YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True


@require_authenticated_permission(
    'blog.add_post')
class PostCreate(PostFormValidMixin, CreateView):
    form_class = PostForm
    model = Post


@require_authenticated_permission(
    'blog.delete_post')
class PostDelete(DateObjectMixin, DeleteView):
    date_field = 'pub_date'
    model = Post
    success_url = reverse_lazy('blog_post_list')


class PostDetail(DateObjectMixin, DetailView):
    date_field = 'pub_date'
    queryset = (
        Post.objects
        .select_related('author__profile')
        .prefetch_related('startups')
        .prefetch_related('tags')
    )


class PostList(
        AllowFuturePermissionMixin,
        ArchiveIndexView):
    allow_empty = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'


@require_authenticated_permission(
    'blog.change_post')
class PostUpdate(
        PostFormValidMixin,
        DateObjectMixin,
        UpdateView):
    date_field = 'pub_date'
    form_class = PostForm
    model = Post
