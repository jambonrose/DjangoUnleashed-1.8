from django.conf import settings
from django.contrib.auth import get_user, logout
from django.contrib.auth.decorators import \
    login_required
from django.shortcuts import redirect
from django.template.response import \
    TemplateResponse
from django.utils.decorators import \
    method_decorator
from django.views.decorators.csrf import \
    csrf_protect
from django.views.generic import View


class DisableAccount(View):
    success_url = settings.LOGIN_REDIRECT_URL
    template_name = (
        'user/user_confirm_delete.html')

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def get(self, request):
        return TemplateResponse(
            request,
            self.template_name)

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def post(self, request):
        user = get_user(request)
        user.set_unusable_password()
        user.is_active = False
        user.save()
        logout(request)
        return redirect(self.success_url)
