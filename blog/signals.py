from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from organizer.models import Tag

from .models import Post


@receiver(m2m_changed,
          sender=Post.startups.through)
def assign_extra_tags(sender, **kwargs):
    action = kwargs.get('action')
    if action == 'post_add':
        reverse = kwargs.get('reverse')
        if not reverse:
            post = kwargs.get('instance')
            # Startup = kwargs.get('model')
            startup_pk_set = kwargs.get('pk_set')
            tag_pk_set = (
                Tag.objects.filter(
                    startup__in=startup_pk_set)
                .values_list('pk', flat=True)
                .distinct().iterator())
            post.tags.add(*tag_pk_set)
        else:
            startup = kwargs.get('instance')
            tag_pk_set = tuple(
                startup.tags.values_list(
                    'pk', flat=True).iterator())
            PostModel = kwargs.get('model')
            post_pk_set = kwargs.get('pk_set')
            posts_dict = (
                PostModel.objects.in_bulk(
                    post_pk_set))
            for post in posts_dict.values():
                post.tags.add(*tag_pk_set)
