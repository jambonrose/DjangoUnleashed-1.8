from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ArchiveIndexView, CreateView, DeleteView,
    DetailView, MonthArchiveView, YearArchiveView)

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


class PostDelete(PostGetMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog_post_list')


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


class PostUpdate(PostGetMixin, UpdateView):
    form_class = PostForm
    model = Post
