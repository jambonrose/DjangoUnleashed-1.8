from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import Context, loader

from .models import Tag


def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template(
        'organizer/tag_list.html')
    context = Context({'tag_list': tag_list})
    output = template.render(context)
    return HttpResponse(output)


def tag_detail(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug)
    template = loader.get_template(
        'organizer/tag_detail.html')
    context = Context({'tag': tag})
    return HttpResponse(template.render(context))
