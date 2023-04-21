from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import User

# Create your models here.


class APIGroups(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class APIClasses(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey("APILables", on_delete=models.CASCADE, blank=True, null=True, related_name="Child_lables")
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    lables = ArrayField(models.PositiveIntegerField(), default=list, blank=True)
    groups = ArrayField(models.PositiveIntegerField(), default=list, blank=True)

    def __str__(self):
        return self.title


class APILables(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    type = models.CharField(max_length=256, blank=True)
    mask = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.title
    

class UserObjects(models.Model):
    classifier_id = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    groups = models.ManyToManyField(APIGroups)
    classes = models.ManyToManyField(APIClasses)
    labels = models.ManyToManyField(APILables)

    class Meta:
        unique_together = ('user', 'classifier_id')

    def __str__(self):
        return f'Classifier {self.classifier_id} for {self.user}'
    
