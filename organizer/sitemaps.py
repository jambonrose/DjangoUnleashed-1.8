from django.contrib.sitemaps import (
    GenericSitemap, Sitemap)

from .models import Startup, Tag

tag_sitemap_dict = {
    'queryset': Tag.objects.all(),
}


TagSitemap = GenericSitemap(tag_sitemap_dict)
