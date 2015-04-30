from django.shortcuts import get_object_or_404

from .models import Post


class PostGetMixin:

    errors = {
        'url_kwargs':
            "Generic view {} must be called with "
            "year, month, and slug.",
    }

    def get_object(self, queryset=None):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        slug = self.kwargs.get('slug')
        if (year is None
                or month is None
                or slug is None):
            raise AttributeError(
                self.errors['url_kwargs'].format(
                    self.__class__.__name__))
        return get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug)
