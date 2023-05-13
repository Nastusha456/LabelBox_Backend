from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import UserObjects
from .serializers import UserObjectsSerializer


class UserObjectsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserObjectsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        id = self.kwargs.get('id')
        if id:
            return UserObjects.objects.filter(user_id=id)
        return UserObjects.objects.none()

    def get_object(self):
        id = self.kwargs.get('id')
        classifier_id_object = self.kwargs.get("pk")
        if id:
            return get_object_or_404(UserObjects, user_id=id, classifier_id=classifier_id_object)
        return get_object_or_404(UserObjects, classifier_id=classifier_id_object)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
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
        