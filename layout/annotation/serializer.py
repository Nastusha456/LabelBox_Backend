from rest_framework import serializers
from .models import APIAnnClasses, APIAnnGroups, APIAnnLables, AnnotationObject

#class AnnWeightSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = AnnWeight
#        fields = ("id", "weight")

class AnnClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIAnnClasses
        fields = ("id", "title",  "code", "lables", "groups")


class AnnLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIAnnLables
        fields = ("id", "title",  "code", "type", "mask")


class AnnGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIAnnGroups
        fields = ('id', 'title', 'code')


class AnnotationObjectSerializer(serializers.ModelSerializer):
    #Weight = AnnWeightSerializer()
    Group = AnnGroupSerializer(many=True)
    Class = AnnClassSerializer(many=True)
    Lables = AnnLabelSerializer(many = True)

    class Meta:
        model = AnnotationObject
        fields = ("user", "Weight", "Group", "Class", "Lables")

    def to_representation(self, instance):
        return super().to_representation(instance)
    
