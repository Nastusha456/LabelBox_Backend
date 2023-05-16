from rest_framework import serializers
from rest_framework.views import APIView
from classificator.models import APIClasses, APILables, APIGroups, UserObjects


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIGroups
        fields = ("id", 'title', 'code')


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIClasses
        fields = ("id", "title",  "code", "lables", "groups")


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = APILables
        fields = ("id", "title",  "code", "type", "mask")


class UserObjectsSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    classes = ClassSerializer(many=True)
    labels = LabelSerializer(many=True)

    class Meta:
        model = UserObjects
        fields = ("user", "groups", "classes", "labels")

    #def to_representation(self, instance):
    #    return super().to_representation(instance)
