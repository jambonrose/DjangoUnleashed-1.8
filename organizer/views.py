from django.shortcuts import (
    get_object_or_404, render)

from .forms import TagForm
from .models import Startup, Tag


def startup_detail(request, slug):
    startup = get_object_or_404(
        Startup, slug__iexact=slug)
    return render(
        request,
        'organizer/startup_detail.html',
        {'startup': startup})


def startup_list(request):
    return render(
        request,
        'organizer/startup_list.html',
        {'startup_list': Startup.objects.all()})


def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            # create new object from data
            # show webpage for new object
            pass
        else:  # empty data or invalid data
            # show bound HTML form (with errors)
            pass
    else:  # request.method != 'POST'
        # show unbound HTML form
        pass


def tag_detail(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag': tag})


def tag_list(request):
    return render(
        request,
        'organizer/tag_list.html',
        {'tag_list': Tag.objects.all()})
