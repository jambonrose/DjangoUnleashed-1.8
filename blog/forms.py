from django import forms
from django.contrib.auth import get_user

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()

    def save(self, request, commit=True):
        post = super().save(commit=False)
        if not post.pk:
            post.author = get_user(request)
        if commit:
            post.save()
            self.save_m2m()
        return post
