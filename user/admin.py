from django.conf.urls import url
from django.contrib import admin
from django.contrib.admin.options import \
    IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import \
    update_session_auth_hash
from django.contrib.auth.forms import \
    AdminPasswordChangeForm
from django.contrib.messages import success
from django.core.exceptions import \
    PermissionDenied
from django.http import (
    Http404, HttpResponseRedirect)
from django.template.response import \
    TemplateResponse
from django.utils.decorators import \
    method_decorator
from django.utils.encoding import force_text
from django.utils.html import escape
from django.views.decorators.debug import \
    sensitive_post_parameters

from .forms import (
    UserChangeForm, UserCreationForm)
from .models import Profile, User


class ProfileAdminInline(admin.StackedInline):
    can_delete = False
    model = Profile
    exclude = ('slug',)

    def view_on_site(self, obj):
        return obj.get_absolute_url()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list view
    actions = ['make_staff']
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
    list_select_related = ('profile',)
    ordering = ('email',)
    search_fields = ('email',)
    # form view
    fieldsets = (
        (None, {
            'fields': ('email', 'password')}),
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
    form = UserChangeForm
    # password
    change_password_form = AdminPasswordChangeForm
    change_user_password_template = (
        'admin/auth/user/change_password.html')

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

    def get_inline_instances(
            self, request, obj=None):
        if obj is None:
            return tuple()
        inline_instance = ProfileAdminInline(
            self.model, self.admin_site)
        return (inline_instance,)

    def get_urls(self):
        password_change = [
            url(r'^(.+)/password/$',
                self.admin_site.admin_view(
                    self.user_change_password),
                name='auth_user_password_change'),
        ]
        urls = super().get_urls()
        urls = password_change + urls
        return urls

    @method_decorator(sensitive_post_parameters())
    def user_change_password(
            self, request, user_id, form_url=''):
        if not self.has_change_permission(
                request):
            raise PermissionDenied
        user = self.get_object(
            request, unquote(user_id))
        if user is None:
            raise Http404(
                '{name} object with primary key '
                '{key} does not exist.'.format(
                    name=force_text(
                        self.model
                        ._meta.verbose_name),
                    key=escape(user_id)))
        if request.method == 'POST':
            form = self.change_password_form(
                user, request.POST)
            if form.is_valid():
                form.save()
                change_message = (
                    self.construct_change_message(
                        request, form, None))
                self.log_change(
                    request, user, change_message)
                success(
                    request, 'Password changed.')
                update_session_auth_hash(
                    request, form.user)
                return HttpResponseRedirect('..')
        else:
            form = self.change_password_form(user)

        context = {
            'title': 'Change password: {}'.format(
                escape(user.get_username())),
            'form_url': form_url,
            'form': form,
            'is_popup': (
                IS_POPUP_VAR in request.POST
                or IS_POPUP_VAR in request.GET),
            'opts': self.model._meta,
            'original': user,
        }
        context.update(
            admin.site.each_context(request))

        request.current_app = self.admin_site.name

        return TemplateResponse(
            request,
            self.change_user_password_template,
            context)

    def make_staff(self, request, queryset):
        rows_updated = queryset.update(
            is_staff=True)
        if rows_updated == 1:
            message = '1 user was'
        else:
            message = '{} users were'.format(
                rows_updated)
        message += ' successfully made staff.'
        self.message_user(request, message)
    make_staff.short_description = (
        'Allow user to access Admin Site.')
