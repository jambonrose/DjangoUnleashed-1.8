from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView)

from core.utils import UpdateView

from .forms import (
    NewsLinkForm, StartupForm, TagForm)
from .models import NewsLink, Startup, Tag
from .utils import (
    NewsLinkGetObjectMixin, PageLinksMixin,
    StartupContextMixin)


class NewsLinkCreate(
        NewsLinkGetObjectMixin,
        StartupContextMixin,
        CreateView):
    form_class = NewsLinkForm
    model = NewsLink


class NewsLinkDelete(
        NewsLinkGetObjectMixin,
        StartupContextMixin,
        DeleteView):
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'

    def get_success_url(self):
        return (self.object.startup
                .get_absolute_url())


class NewsLinkUpdate(
        NewsLinkGetObjectMixin,
        StartupContextMixin,
        UpdateView):
    form_class = NewsLinkForm
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'


class StartupCreate(CreateView):
    form_class = StartupForm
    model = Startup


class StartupDelete(DeleteView):
    model = Startup
    success_url = reverse_lazy(
        'organizer_startup_list')


class StartupDetail(DetailView):
    model = Startup


class StartupList(PageLinksMixin, ListView):
    model = Startup
    paginate_by = 5  # 5 items per page


class StartupUpdate(UpdateView):
    form_class = StartupForm
    model = Startup


class TagCreate(CreateView):
    form_class = TagForm
    model = Tag


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy(
        'organizer_tag_list')


class TagDetail(DetailView):
    model = Tag


class TagList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Tag


class TagUpdate(UpdateView):
    form_class = TagForm
    model = Tag
