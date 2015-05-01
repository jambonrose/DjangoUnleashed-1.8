from django.contrib.auth.decorators import (
    login_required, permission_required)
from django.utils.decorators import \
    method_decorator


def custom_login_required(view):
    # view argument must be a method
    decorator = method_decorator(login_required)
    decorated_view = decorator(view)
    return decorated_view


def require_authenticated_permission(permission):

    def decorator(view):
        # view must be a function
        check_auth = login_required
        check_perm = (
            permission_required(
                permission, raise_exception=True))

        decorated_view = (
            check_auth(check_perm(view)))
        return decorated_view

    return decorator
