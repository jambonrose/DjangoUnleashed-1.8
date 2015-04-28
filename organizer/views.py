from django.core.paginator import (
    EmptyPage, PageNotAnInteger, Paginator)
from django.core.urlresolvers import (
    reverse, reverse_lazy)
from django.shortcuts import render
from django.views.generic import (
    CreateView, DeleteView,
    DetailView, UpdateView, View)

from .forms import (
    NewsLinkForm, StartupForm, TagForm)
from .models import NewsLink, Startup, Tag


class NewsLinkCreate(CreateView):
    form_class = NewsLinkForm
    model = NewsLink


class NewsLinkDelete(DeleteView):
    model = NewsLink

    def get_success_url(self):
        return (self.object.startup
                .get_absolute_url())


class NewsLinkUpdate(UpdateView):
    form_class = NewsLinkForm
    model = NewsLink
    template_name_suffix = '_form_update'


class StartupCreate(CreateView):
    form_class = StartupForm
    model = Startup


class StartupDelete(DeleteView):
    model = Startup
    success_url = reverse_lazy(
        'organizer_startup_list')


class StartupDetail(DetailView):
    model = Startup


class StartupList(View):
    page_kwarg = 'page'
    paginate_by = 5  # 5 items per page
    template_name = 'organizer/startup_list.html'

    def get(self, request):
        startups = Startup.objects.all()
        paginator = Paginator(
            startups, self.paginate_by)
        page_number = request.GET.get(
            self.page_kwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(
                pkw=self.page_kwarg,
                n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated':
                page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'startup_list': page,
        }
        return render(
            request, self.template_name, context)


class StartupUpdate(UpdateView):
    form_class = StartupForm
    model = Startup
    template_name = (
        'organizer/startup_form_update.html')


class TagCreate(CreateView):
    form_class = TagForm
    model = Tag


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy(
        'organizer_tag_list')


class TagDetail(DetailView):
    model = Tag


class TagList(View):
    template_name = 'organizer/tag_list.html'

    def get(self, request):
        tags = Tag.objects.all()
        context = {
            'tag_list': tags,
        }
        return render(
            request, self.template_name, context)


class TagPageList(View):
    paginate_by = 5
    template_name = 'organizer/tag_list.html'

    def get(self, request, page_number):
        tags = Tag.objects.all()
        paginator = Paginator(
            tags, self.paginate_by)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages)
        if page.has_previous():
            prev_url = reverse(
                'organizer_tag_page',
                args=(
                    page.previous_page_number(),
                ))
        else:
            prev_url = None
        if page.has_next():
            next_url = reverse(
                'organizer_tag_page',
                args=(
                    page.next_page_number(),
                ))
        else:
            next_url = None
        context = {
            'is_paginated':
                page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'tag_list': page,
        }
        return render(
            request, self.template_name, context)


class TagUpdate(UpdateView):
    form_class = TagForm
    model = Tag
    template_name = (
        'organizer/tag_form_update.html')
