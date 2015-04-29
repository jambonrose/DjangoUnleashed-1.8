from django.shortcuts import get_object_or_404

from .models import Post


class PostGetMixin:

    def get_object(self, queryset=None):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        slug = self.kwargs.get('slug')
        return get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug__iexact=slug)
