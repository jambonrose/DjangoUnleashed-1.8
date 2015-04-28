from django.core.paginator import (
    EmptyPage, PageNotAnInteger, Paginator)
from django.core.urlresolvers import (
    reverse, reverse_lazy)
from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import DetailView, View

from .forms import (
    NewsLinkForm, StartupForm, TagForm)
from .models import NewsLink, Startup, Tag
from .utils import (
    ObjectCreateMixin, ObjectDeleteMixin,
    ObjectUpdateMixin)


class NewsLinkCreate(ObjectCreateMixin, View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'


class NewsLinkDelete(View):

    def get(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk)
        return render(
            request,
            'organizer/'
            'newslink_confirm_delete.html',
            {'newslink': newslink})

    def post(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk)
        startup = newslink.startup
        newslink.delete()
        return redirect(startup)


class NewsLinkUpdate(View):
    form_class = NewsLinkForm
    template_name = (
        'organizer/newslink_form_update.html')

    def get(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk)
        context = {
            'form': self.form_class(
                instance=newslink),
            'newslink': newslink,
        }
        return render(
            request, self.template_name, context)

    def post(self, request, pk):
        newslink = get_object_or_404(
            NewsLink, pk=pk)
        bound_form = self.form_class(
            request.POST, instance=newslink)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            context = {
                'form': bound_form,
                'newslink': newslink,
            }
            return render(
                request,
                self.template_name,
                context)


class StartupCreate(ObjectCreateMixin, View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'


class StartupDelete(ObjectDeleteMixin, View):
    model = Startup
    success_url = reverse_lazy(
        'organizer_startup_list')
    template_name = (
        'organizer/startup_confirm_delete.html')


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


class StartupUpdate(ObjectUpdateMixin, View):
    form_class = StartupForm
    model = Startup
    template_name = (
        'organizer/startup_form_update.html')


class TagCreate(ObjectCreateMixin, View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    success_url = reverse_lazy(
        'organizer_tag_list')
    template_name = (
        'organizer/tag_confirm_delete.html')


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


class TagUpdate(ObjectUpdateMixin, View):
    form_class = TagForm
    model = Tag
    template_name = (
        'organizer/tag_form_update.html')
