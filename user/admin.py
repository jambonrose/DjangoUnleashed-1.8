from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list view
    list_display = (
        'email',
        'get_date_joined',
        'is_staff',
        'is_superuser')
    list_filter = (
        'is_staff',
        'is_superuser',
        'profile__joined')
    ordering = ('email',)
    search_fields = ('email',)

    def get_date_joined(self, user):
        return user.profile.joined
    get_date_joined.short_description = 'Joined'
    get_date_joined.admin_order_field = (
        'profile__joined')
