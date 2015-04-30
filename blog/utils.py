from django.shortcuts import get_object_or_404

from .models import Post


class PostGetMixin:
    date_field = 'pub_date'
    model = Post
    month_url_kwarg = 'month'
    year_url_kwarg = 'year'

    errors = {
        'url_kwargs':
            "Generic view {} must be called with "
            "year, month, and slug.",
        'not_exist':
            "No {} by that date and slug.",
    }

    def get_object(self, queryset=None):
        year = self.kwargs.get(
            self.year_url_kwarg)
        month = self.kwargs.get(
            self.month_url_kwarg)
        slug = self.kwargs.get(
            self.slug_url_kwarg)
        if (year is None
                or month is None
                or slug is None):
            raise AttributeError(
                self.errors['url_kwargs'].format(
                    self.__class__.__name__))
        date_field = self.date_field
        slug_field = self.get_slug_field()
        filter_dict = {
            date_field + '__year': year,
            date_field + '__month': month,
            slug_field: slug,
        }
        if queryset is None:
            queryset = self.get_queryset()
        queryset = queryset.filter(**filter_dict)
        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404(
                self.errors['not_exist'].format(
                    queryset.model
                    ._meta.verbose_name))
        return obj
