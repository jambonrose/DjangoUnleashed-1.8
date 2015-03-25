from django.contrib.sitemaps import (
    GenericSitemap, Sitemap)

from .models import Startup, Tag

tag_sitemap_dict = {
    'queryset': Tag.objects.all(),
}


TagSitemap = GenericSitemap(tag_sitemap_dict)


class StartupSitemap(Sitemap):

    def items(self):
        return Startup.objects.all()

    def lastmod(self, startup):
        if startup.newslink_set.exists():
            return (
                startup.newslink_set.latest()
                .pub_date)
        else:
            return startup.founded_date
