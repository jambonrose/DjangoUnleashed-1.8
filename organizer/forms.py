from django import forms


class TagForm(forms.Form):
    name = forms.CharField(max_length=31)
    slug = forms.SlugField(
        max_length=31,
        help_text='A label for URL config')
