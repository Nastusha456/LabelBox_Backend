from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from classificator.models import UserObjects
from django.db.models import Max
from users.models import User

@receiver(pre_save, sender=UserObjects)
def set_classifier_id(sender, instance, **kwargs):
    if not instance.classifier_id:
        # Если у аннотации нет ID, то ищем максимальный среди уже созданных
        max_id = UserObjects.objects.filter(user=instance.user).aggregate(max_id=Max('classifier_id'))['max_id']
        instance.classifier_id = 1 if max_id is None else max_id + 1


@receiver(post_save, sender=User)
def create_user_classifier(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        classifier_object = UserObjects.objects.create(user=instance)
        set_classifier_id(sender=UserObjects, instance=classifier_object)