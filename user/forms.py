from django.contrib.auth import get_user_model
from django.contrib.auth.forms import \
    UserCreationForm as BaseUserCreationForm

from .utils import ActivationMailFormMixin


class UserCreationForm(
        ActivationMailFormMixin,
        BaseUserCreationForm):

    mail_validation_error = (
        'User created. Could not send activation '
        'email. Please try again later. (Sorry!)')

    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')

    def save(self, **kwargs):
        user = super().save(commit=False)
        if not user.pk:
            user.is_active = False
            send_mail = True
        else:
            send_mail = False
        user.save()
        self.save_m2m()
        if send_mail:
            self.send_mail(user=user, **kwargs)
        return user
