from django.db import models
from django.contrib.postgres.fields import ArrayField
#import classificator
from users.models import User

# Create your models here.

#class AnnWeight(models.Model):
#    id = models.AutoField(primary_key=True)
#    #user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, default=None)
#    weight = models.CharField(max_length=256)


class APIAnnGroups(models.Model):
    id = models.AutoField(primary_key=True)
    #user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, default=None)
    position_x = ArrayField(models.IntegerField(), default=list, blank=True)
    position_y = ArrayField(models.IntegerField(), default=list, blank=True)
    color = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256)

    def __str__(self):
        return self.title
    

class APIAnnClasses(models.Model):
    id = models.AutoField(primary_key=True)
    #user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, default=None)
    position_x = ArrayField(models.IntegerField(), default=list, blank=True)
    position_y = ArrayField(models.IntegerField(), default=list, blank=True)
    color = models.CharField(max_length=256, null=True)
    parent = models.ForeignKey("APIAnnLables", on_delete=models.PROTECT, blank=True, null=True, related_name="Child_lables")
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    lables = ArrayField(models.PositiveIntegerField(), default=list, blank=True)
    groups = ArrayField(models.PositiveIntegerField(), default=list, blank=True)

    def __str__(self):
        return self.title
    


class APIAnnLables(models.Model):
    id = models.AutoField(primary_key=True)
    #user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, default=None)
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
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, default=None)
    #Weight = models.ForeignKey(AnnWeight, on_delete=models.PROTECT, null=True, blank=True, default=None)
    Group = models.ManyToManyField(APIAnnGroups)
    Class = models.ManyToManyField(APIAnnClasses)
    Lables = models.ManyToManyField(APIAnnLables)

    class Meta:
        unique_together = ('user', 'annotation_id')

    def __str__(self):
        return f'Annotation {self.annotation_id} for {self.user}'