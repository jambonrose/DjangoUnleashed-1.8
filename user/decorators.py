from django.contrib.auth.decorators import \
    login_required
from django.utils.decorators import \
    method_decorator


def custom_login_required(view):
    # view argument must be a method
    decorator = method_decorator(login_required)
    decorated_view = decorator(view)
    return decorated_view
