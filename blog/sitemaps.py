from datetime import date
from math import log10

from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):
    changefreq = "never"

    def items(self):
        return Post.objects.published()

    def lastmod(self, post):
        return post.pub_date

    def priority(self, post):
        """Returns numerical priority of post.

        1.0 is most important
        0.0 is least important
        0.5 is the default
        """
        period = 90  # days
        timedelta = date.today() - post.pub_date
        # 86400 seconds in a day
        # 86400 = 60 seconds * 60 minutes * 24 hours
        # use floor division
        days = timedelta.total_seconds() // 86400
        if days == 0:
            return 1.0
        elif 0 < days <= period:
            # n(d) = normalized(days)
            # n(1) = 0.5
            # n(period) = 0
            normalized = (
                log10(period / days) /
                log10(period ** 2))
            normalized = round(normalized, 2)
            return normalized + 0.5
        else:
            return 0.5
