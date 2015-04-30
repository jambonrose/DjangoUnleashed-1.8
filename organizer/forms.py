from django import forms
from django.core.exceptions import ValidationError

from .models import NewsLink, Startup, Tag


class SlugCleanMixin:
    """Mixin class for slug cleaning method."""

    def clean_slug(self):
        new_slug = (
            self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError(
                'Slug may not be "create".')
        return new_slug


class NewsLinkForm(
        SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = NewsLink
        exclude = ('startup',)

    def clean(self):
        cleaned_data = super().clean()
        slug = cleaned_data.get('slug')
        startup_obj = self.data.get('startup')
        exists = (
            NewsLink.objects.filter(
                slug__iexact=slug,
                startup=startup_obj,
            ).exists())
        if exists:
            raise ValidationError(
                "News articles with this Slug "
                "and Startup already exists.")
        else:
            return cleaned_data

    def save(self, **kwargs):
        instance = super().save(commit=False)
        instance.startup = (
            self.data.get('startup'))
        instance.save()
        self.save_m2m()
        return instance


class StartupForm(
        SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'


class TagForm(
        SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()
