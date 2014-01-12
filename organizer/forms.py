from django import forms
from django.core.exceptions import ValidationError

from .models import Tag


class TagForm(forms.Form):
    name = forms.CharField(max_length=31)
    slug = forms.SlugField(
        max_length=31,
        help_text='A label for URL config')

    def clean_name(self):
        return self.cleaned_data['name'].lower()

    def clean_slug(self):
        new_slug = (
            self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError(
                'Slug may not be "create".')
        return new_slug

    def save(self):
        new_tag = Tag.objects.create(
            name=self.cleaned_data['name'],
            slug=self.cleaned_data['slug'])
        return new_tag
