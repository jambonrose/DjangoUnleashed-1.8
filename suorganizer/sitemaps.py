from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from blog.sitemaps import (
    PostArchiveSitemap, PostSitemap)
from organizer.sitemaps import (
    StartupSitemap, TagSitemap)


class RootSitemap(Sitemap):
    priority = 0.6

    def items(self):
        return [
            'about_site',
            'blog_post_list',
            'contact',
            'dj_auth:login'
            'organizer_startup_list',
            'organizer_tag_list',
        ]

    def location(self, url_name):
        return reverse(url_name)


sitemaps = {
    'post-archives': PostArchiveSitemap,
    'posts': PostSitemap,
    'roots': RootSitemap,
    'startups': StartupSitemap,
    'tags': TagSitemap,
}
