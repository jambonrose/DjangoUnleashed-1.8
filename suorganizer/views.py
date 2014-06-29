from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def redirect_root(request):
    url_path = reverse('blog_post_list')
    return HttpResponseRedirect(url_path)
