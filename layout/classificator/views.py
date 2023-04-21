from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import generics
from classificator.models import APIClasses, APIGroups, APILables, UserObjects
from .serializers import ClassSerializer, GroupSerializer, LabelSerializer, UserObjectsSerializer
from rest_framework import permissions, authentication
import json

# Create your views here.

class UserObjectsView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserObjectsSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            return UserObjects.objects.filter(user=user_id)
        return UserObjects.objects.none()

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        classifier_id_object = self.kwargs.get("pk")
        if user_id:
            return get_object_or_404(UserObjects, user=user_id, classifier_id=classifier_id_object)
        return get_object_or_404(UserObjects, classifier_id=classifier_id_object)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

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