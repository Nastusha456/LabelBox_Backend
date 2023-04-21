from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from annotation.models import AnnotationObject
from django.db.models import Max
from users.models import User

@receiver(pre_save, sender=AnnotationObject)
def set_annotation_id(sender, instance, **kwargs):
    if not instance.annotation_id:
        # Если у аннотации нет ID, то ищем максимальный среди уже созданных
        max_id = AnnotationObject.objects.filter(user=instance.user).aggregate(max_id=Max('annotation_id'))['max_id']
        instance.annotation_id = 1 if max_id is None else max_id + 1


@receiver(post_save, sender=User)
def create_user_annotation(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        annotation_object = AnnotationObject.objects.create(user=instance)
        set_annotation_id(sender=AnnotationObject, instance=annotation_object)
