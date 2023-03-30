from rest_framework import serializers
from classificator.models import APIClasses, APILables, APIGroups

class ClassificatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIClasses
        fields = ("title",  "code", "lables", "groups")


#class LabelSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = APILables
#        fields = ("title",  "code", "type", "mask")
#
#class GroupSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = APIGroups
#        fields = ("title",  "code")