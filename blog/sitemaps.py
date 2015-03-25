from datetime import date
from itertools import chain
from math import log10
from operator import itemgetter

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

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


class PostArchiveSitemap(Sitemap):

    def items(self):
        year_dates = (
            Post.objects.published().dates(
                'pub_date', 'year', order='DESC',
            ).iterator())
        month_dates = (
            Post.objects.published().dates(
                'pub_date', 'month', order='DESC',
            ).iterator())
        year_tuples = map(
            lambda d: (d, 'y'),
            year_dates)
        month_tuples = map(
            lambda d: (d, 'm'),
            month_dates)
        return sorted(
            chain(month_tuples, year_tuples),
            key=itemgetter(0),
            reverse=True)

    def location(self, date_tuple):
        archive_date, archive_type = date_tuple
        if archive_type == 'y':
            return reverse(
                'blog_post_archive_year',
                kwargs={
                    'year': archive_date.year})
        elif archive_type == 'm':
            return reverse(
                'blog_post_archive_month',
                kwargs={
                    'year': archive_date.year,
                    'month': archive_date.month})
        else:
            raise NotImplementedError(
                "{} did not recognize "
                "{} denoted '{}'.".format(
                    self.__class__.__name__,
                    'archive_type',
                    archive_type))
