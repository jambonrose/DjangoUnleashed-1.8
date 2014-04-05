from django import forms

from .models import Tag


class TagForm(forms.Form):
    name = forms.CharField(max_length=31)
    slug = forms.SlugField(
        max_length=31,
        help_text='A label for URL config')

    def clean_name(self):
        return self.cleaned_data['name'].lower()

    def save(self):
        new_tag = Tag.objects.create(
            name=self.cleaned_data['name'],
            slug=self.cleaned_data['slug'])
        return new_tag
