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

    def save(self, **kwargs):
        startup_obj = kwargs.get('startup_obj', None)
        if startup_obj is not None:
            instance = super().save(commit=False)
            instance.startup = startup_obj
            instance.save()
            self.save_m2m()
        else:
            instance = super().save()
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
