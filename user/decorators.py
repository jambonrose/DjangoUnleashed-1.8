from django.contrib.auth.decorators import \
    login_required


def custom_login_required(view):
    # view argument must be a function
    decorated_view = login_required(view)
    return decorated_view
