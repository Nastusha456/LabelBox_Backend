from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from django.views.decorators.csrf import csrf_exempt
from .models import AnnotationObject
from .serializer import AnnotationObjectSerializer
from rest_framework.response import Response


class AnnotationObjectView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnnotationObjectSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            return AnnotationObject.objects.filter(user=user_id)
        return AnnotationObject.objects.none()

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        annotation_id_object = self.kwargs.get("pk")
        if user_id:
            return get_object_or_404(AnnotationObject, user=user_id, annotation_id=annotation_id_object)
        return get_object_or_404(AnnotationObject, annotation_id=annotation_id_object)

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
        serializer = self.serializer_class(
            instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
