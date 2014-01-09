from django.http import HttpResponseRedirect


def redirect_root(request):
    return HttpResponseRedirect('/blog/')
