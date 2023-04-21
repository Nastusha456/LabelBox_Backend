from django.contrib import admin
from .models import APIClasses, APIGroups, APILables, UserObjects
# Register your models here.
admin.site.register(APIGroups)
admin.site.register(APIClasses)
admin.site.register(APILables)
admin.site.register(UserObjects)
