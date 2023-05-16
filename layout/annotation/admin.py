from django.contrib import admin
from .models import APIAnnClasses, APIAnnGroups, APIAnnLables, AnnotationObject

admin.site.register(AnnotationObject)
admin.site.register(APIAnnGroups)
admin.site.register(APIAnnClasses)
admin.site.register(APIAnnLables)