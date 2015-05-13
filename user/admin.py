from django.contrib import admin

from .forms import UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list view
    list_display = (
        'get_name',
        'email',
        'get_date_joined',
        'is_staff',
        'is_superuser')
    list_display_links = ('get_name', 'email')
    list_filter = (
        'is_staff',
        'is_superuser',
        'profile__joined')
    ordering = ('email',)
    search_fields = ('email',)
    # form view
    fieldsets = (
        (None, {
            'fields': ('email',)}),
        ('Permissions', {
            'classes': ('collapse',),
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions')}),
        ('Important dates', {
            'classes': ('collapse',),
            'fields': ('last_login',)}),
    )
    filter_horizontal = (
        'groups', 'user_permissions',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name',
                'email',
                'password1',
                'password2')
        }),
    )
    add_form = UserCreationForm

    def get_date_joined(self, user):
        return user.profile.joined
    get_date_joined.short_description = 'Joined'
    get_date_joined.admin_order_field = (
        'profile__joined')

    def get_name(self, user):
        return user.profile.name
    get_name.short_description = 'Name'
    get_name.admin_order_field = 'profile__name'

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def get_form(
            self, request, obj=None, **kwargs):
        if obj is None:
            kwargs['form'] = self.add_form
        return super().get_form(
            request, obj, **kwargs)
