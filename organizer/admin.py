from django.contrib import admin

from .models import NewsLink, Startup, Tag

admin.site.register(NewsLink)
admin.site.register(Startup)
admin.site.register(Tag)
