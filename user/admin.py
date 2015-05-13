from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list view
    list_display = (
        'email',
        'is_staff',
        'is_superuser')
    list_filter = (
        'is_staff',
        'is_superuser',
        'profile__joined')
    ordering = ('email',)
    search_fields = ('email',)
