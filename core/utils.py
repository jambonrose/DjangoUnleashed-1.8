from django.views.generic import \
    UpdateView as BaseUpdateView


class UpdateView(BaseUpdateView):
    template_name_suffix = '_form_update'
