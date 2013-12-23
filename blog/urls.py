from django.conf.urls import url

from .views import post_detail, post_list

urlpatterns = [
    url(r'^$',
        post_list,
        name='blog_post_list'),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/$',
        post_detail,
        name='blog_post_detail'),
]
