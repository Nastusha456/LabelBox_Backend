from rest_framework import serializers
from rest_framework.views import APIView
from classificator.models import APIClasses, APILables, APIGroups, UserObjects
from rest_framework.response import Response

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
    labels = LabelSerializer(many = True)

    class Meta:
        model = UserObjects
        fields = ("user", "groups", "classes", "labels")

    def to_representation(self, instance):
        return super().to_representation(instance)

# class CombinedSerializer(serializers.Serializer):
#     Class = ClassSerializer(many=True)
#     Groups = GroupSerializer(many=True)
#     Labels = LabelSerializer(many=True)

#     def to_representation(self, instance):
#         Class = instance['Class']
#         Groups = instance['Groups']
#         Labels = instance['Lables']
#         return {
#             'Class': ClassSerializer(Class, many=True).data,
#             'Groups': GroupSerializer(Groups, many=True).data,
#             'Labels': LabelSerializer(Labels, many=True).data
#         }

# class CombinedAPIView(APIView):
#     def get(self, request):
#         Classes = APIClasses.objects.all()
#         Groups = APIGroups.objects.all()

#         serializer = CombinedSerializer(
#             {"classes": Classes, "groups": Groups})
#         return Response(serializer.data)
