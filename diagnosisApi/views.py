from django.shortcuts import render
from diagnosisApi.serializers import DiagnosisSerializer, CategorySerializer
from diagnosisApi.models import Diagnosis, Category

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class DiagnosisList(generics.ListCreateAPIView):
     #permission_classes = (IsAuthenticated,)
     queryset = Diagnosis.objects.all()
     serializer_class = DiagnosisSerializer

class DiagnosisDetail(generics.RetrieveUpdateDestroyAPIView):
     #permission_classes = (IsAuthenticated,)
     queryset = Diagnosis.objects.all()
     serializer_class = DiagnosisSerializer

class CategoryList(generics.ListCreateAPIView):
     #permission_classes = (IsAuthenticated,)
     queryset = Category.objects.all()
     serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
     #permission_classes = (IsAuthenticated,)
     queryset = Category.objects.all()
     serializer_class = CategorySerializer
