from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import User


class APIAnnGroups(models.Model):
    id = models.AutoField(primary_key=True)
    position_x = ArrayField(models.IntegerField(), default=list, blank=True)
    position_y = ArrayField(models.IntegerField(), default=list, blank=True)
    color = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class APIAnnClasses(models.Model):
    id = models.AutoField(primary_key=True)
    position_x = ArrayField(models.IntegerField(), default=list, blank=True)
    position_y = ArrayField(models.IntegerField(), default=list, blank=True)
    color = models.CharField(max_length=256, null=True)
    parent = models.ForeignKey("APIAnnLables", on_delete=models.CASCADE,
                               blank=True, null=True, related_name="Child_lables")
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    lables = ArrayField(models.PositiveIntegerField(),
                        default=list, blank=True)
    groups = ArrayField(models.PositiveIntegerField(),
                        default=list, blank=True)

    def __str__(self):
        return self.title


class APIAnnLables(models.Model):
    id = models.AutoField(primary_key=True)
    position_x = ArrayField(models.IntegerField(), default=list, blank=True)
    position_y = ArrayField(models.IntegerField(), default=list, blank=True)
    color = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    type = models.CharField(max_length=256, blank=True)
    mask = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.title


class AnnotationObject(models.Model):
    annotation_id = models.PositiveIntegerField(default=1)
    Weight = models.CharField(max_length=256, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True, default=None, related_name='annotations')
    Group = models.ManyToManyField(APIAnnGroups)
    Class = models.ManyToManyField(APIAnnClasses)
    Lables = models.ManyToManyField(APIAnnLables)

    class Meta:
        unique_together = ('user', 'annotation_id')

    def __str__(self):
        return f'Annotation {self.annotation_id} for {self.user}'
