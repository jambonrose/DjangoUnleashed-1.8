from django.contrib.auth.decorators import (
    login_required, permission_required)
from django.core.exceptions import \
    ImproperlyConfigured
from django.utils.decorators import \
    method_decorator
from django.views.generic import View


def class_login_required(cls):
    if (not isinstance(cls, type)
            or not issubclass(cls, View)):
        raise ImproperlyConfigured(
            "class_login_required"
            " must be applied to subclasses "
            "of View class.")
    decorator = method_decorator(login_required)
    cls.dispatch = decorator(cls.dispatch)
    return cls


def require_authenticated_permission(permission):

    def decorator(cls):
        if (not isinstance(cls, type)
                or not issubclass(cls, View)):
            raise ImproperlyConfigured(
                "require_authenticated_permission"
                " must be applied to subclasses "
                "of View class.")
        check_auth = (
            method_decorator(login_required))
        check_perm = (
            method_decorator(
                permission_required(
                    permission,
                    raise_exception=True)))

        cls.dispatch = (
            check_auth(check_perm(cls.dispatch)))
        return cls

    return decorator
