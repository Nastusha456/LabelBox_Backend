from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from classificator.models import APIClasses, APIGroups, APILables, UserObjects
from .serializers import ClassSerializer, GroupSerializer, LabelSerializer, UserObjectsSerializer
from rest_framework import permissions, authentication
import json

# Create your views here.

class UserObjectsView(generics.ListCreateAPIView):
    serializer_class = UserObjectsSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        classifier_object_id = self.kwargs.get('pk')
        if user_id:
            return UserObjects.objects.filter(user=user_id, id=classifier_object_id)
        return UserObjects.objects.none()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return HttpResponse(status=404)
        serializer = self.serializer_class(queryset.first())
        data = serializer.data
        json_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(json_data, content_type="application/json")
        #return JsonResponse(json_data, safe=False)

## то, что работало, пока я не объеденил части классификатора в один большой классификатор

# class TotalAPIView(APIView):
#     def get(self, request):
#         authentication_classes = (authentication.TokenAuthentication,)
#         permission_classes = (permissions.IsAuthenticated,)

#         class_result = APIClasses.objects.filter(user=request.user.id)
#         groups_result = APIGroups.objects.filter(user=request.user.id)
#         labels_result = APILables.objects.filter(user=request.user.id)

#         Class_serializer = ClassSerializer(class_result, many=True).data
#         Group_serializer = GroupSerializer(groups_result, many=True).data
#         Label_serializer = LabelSerializer(labels_result, many=True).data

#         data = {
#             "groups": Group_serializer,
#             "classes": Class_serializer,
#             "labels": Label_serializer,
#         }
#         return Response(data)
    
#     def post(self, request):
#         pass
##


# class ClassAPIView(generics.ListAPIView):
#     queryset = APIClasses.objects.all() #, APILables.objects.all(), APIGroups.objects.all()}
#     serializer_class = ClassSerializer

# class LabelAPIView(generics.ListAPIView):
#     queryset = APILables.objects.all()
#     serializer_class = LabelSerializer