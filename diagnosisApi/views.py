from django.shortcuts import render
from diagnosisApi.serializers import DiagnosisSerializer
from diagnosisApi.models import Diagnosis

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
