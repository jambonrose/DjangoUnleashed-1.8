from datetime import date

from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5  # default value

    def items(self):
        return Post.objects.published()

    def lastmod(self, post):
        return post.pub_date
