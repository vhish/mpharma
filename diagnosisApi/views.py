from django.shortcuts import render
from diagnosisApi.serializers import DiagnosisSerializer
from diagnosisApi.models import Diagnosis

from rest_framework import generics



class DiagnosisList(generics.ListCreateAPIView):
     queryset = Diagnosis.objects.all()
     serializer_class = DiagnosisSerializer

class DiagnosisDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Diagnosis.objects.all()
     serializer_class = DiagnosisSerializer
