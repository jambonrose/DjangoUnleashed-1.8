from django.conf import settings
from django.contrib.auth import get_user
from django.shortcuts import redirect


def custom_login_required(view):
    # view argument must be a function

    def new_view(request, *args, **kwargs):
        user = get_user(request)
        if user.is_authenticated():
            return view(request, *args, **kwargs)
        else:
            url = '{}?next={}'.format(
                settings.LOGIN_URL,
                request.path)
            return redirect(url)

    return new_view
