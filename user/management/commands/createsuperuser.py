from django.utils.text import slugify

from user.models import Profile

from .createuser import Command as BaseCommand


class Command(BaseCommand):
    help = 'Create new Super User with Profile.'

    def create_user(
            self, name, username, password):
        new_user = (
            self.User.objects.create_superuser(
                username, password))
        try:
            Profile.objects.create(
                user=new_user,
                name=name,
                slug=slugify(name))
        except Exception as e:
            raise CommandError(
                "Could not create Profile:\n{}"
                .format('; '.join(e.messages)))
