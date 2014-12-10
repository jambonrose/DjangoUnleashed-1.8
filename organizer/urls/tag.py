from django.conf.urls import url

from ..views import (
    TagCreate, TagDelete, TagList, TagPageList,
    TagUpdate, tag_detail)

urlpatterns = [
    url(r'^$',
        TagList.as_view(),
        name='organizer_tag_list'),
    url(r'^create/$',
        TagCreate.as_view(),
        name='organizer_tag_create'),
    url(r'^(?P<page_number>\d+)/$',
        TagPageList.as_view(),
        name='organizer_tag_page'),
    url(r'^(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='organizer_tag_detail'),
    url(r'^(?P<slug>[\w-]+)/delete/$',
        TagDelete.as_view(),
        name='organizer_tag_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$',
        TagUpdate.as_view(),
        name='organizer_tag_update'),
]
