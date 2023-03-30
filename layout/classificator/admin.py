from django.contrib import admin
from .models import APIClasses, APIGroups, APILables
# Register your models here.
admin.site.register(APIClasses)
admin.site.register(APILables)
admin.site.register(APIGroups)