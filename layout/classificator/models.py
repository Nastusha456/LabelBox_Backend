from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class APIGroups(models.Model):
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class APILables(models.Model):
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    type = models.CharField(max_length=256, blank=True)
    mask = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.title


class APIClasses(models.Model):
    #parent = models.ForeignKey(APILables, on_delete=models.PROTECT, blank=True)
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    lables = models.ManyToManyField(APILables, blank=True)
    groups = models.ManyToManyField(APIGroups, blank=True)

    def __str__(self):
        return self.title
