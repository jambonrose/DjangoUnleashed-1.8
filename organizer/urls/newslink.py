from django.conf.urls import url

from ..views import (
    NewsLinkCreate, NewsLinkDelete,
    NewsLinkUpdate)

urlpatterns = [
    url(r'^create/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),
    url(r'^delete/(?P<pk>\d+)/$',
        NewsLinkDelete.as_view(),
        name='organizer_newslink_delete'),
    url(r'^update/(?P<pk>\d+)/$',
        NewsLinkUpdate.as_view(),
        name='organizer_newslink_update'),
]
