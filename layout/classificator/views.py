from django.shortcuts import render
from rest_framework import generics
from classificator.models import APIClasses
from .serializers import ClassificatorSerializer

# Create your views here.
class ClassificatorAPIView(generics.ListAPIView):
    queryset = APIClasses.objects.all()
    serializer_class = ClassificatorSerializer