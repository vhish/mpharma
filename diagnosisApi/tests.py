import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import Diagnosis, Category
from .serializers import DiagnosisSerializer, CategorySerializer

# initialize the APIClient app
client = Client()

# Create your tests here.
class GetAllDiagnosisList(TestCase):
    """ Test module for GET paginated list of diagnosis """

    def setUp(self):
        Category.objects.create(
            category_code='A1', category_title='Internal Bleeding'
        )
        Category.objects.create(
            category_code='A2', category_title='Concussion'
        )

        a1  =  Category.objects.get(category_code="A1")
        a2  =  Category.objects.get(category_code="A2")

        Diagnosis.objects.create(
            category=a1,
            full_description='Neuroplasma Melanoma',
            abbreviated_description='NM',
            diagnosis_code=24,
            code_type='icd-9'
        )
        Diagnosis.objects.create(
            category=a2,
            full_description='Anorexia Nemvosa',
            abbreviated_description='NM',
            diagnosis_code=23,
            code_type = 'icd-10'
        )

    def test_get_all_diagnosis(self):
        # get API response
        response = client.get(reverse('diagnosisApi:get_diagnosis_list'))
        # get data from db
        #print("The response data --> " , response.data["results"])
        diagnosis = Diagnosis.objects.all()[:20]
        #for c in diagnosis :
        #    print("diagnosis_code --> " ,  diagnosis.diagnosis_code )
        serializer = DiagnosisSerializer(diagnosis, many=True)
        print("Results -> " , response.data['results'])
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleDiagnosis(TestCase):
    """ Test module for GET paginated list of diagnosis """

    def setUp(self):
        Category.objects.create(
            category_code='A1', category_title='Internal Bleeding'
        )
        Category.objects.create(
            category_code='A2', category_title='Concussion'
        )

        a1  =  Category.objects.get(category_code="A1")
        a2  =  Category.objects.get(category_code="A2")

        self.d1 = Diagnosis.objects.create(
            category=a1,
            full_description='Neuroplasma Melanoma',
            abbreviated_description='NM',
            diagnosis_code=24,
            code_type = 'icd-10'
        )
        self.d2 = Diagnosis.objects.create(
            category=a2,
            full_description='Anorexia Nemvosa',
            abbreviated_description='NM',
            diagnosis_code=23,
            code_type = 'ICD-10'
        )

    def test_get_valid_single_dignosis(self):
        response = client.get(reverse('diagnosisApi:get_diagnosis_detail', kwargs={'pk': self.d1.pk}))
        diagnosis =  Diagnosis.objects.get(id=self.d1.id)
        serializer = DiagnosisSerializer(diagnosis)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_invalid_single_dignosis(self):
        response = client.get(reverse('diagnosisApi:get_diagnosis_detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewDiganosis(TestCase):
    """ Test module for creating a new diagnosis code"""

    def setUp(self):
        Category.objects.create(
            category_code='A2', category_title='Concussion'
        )

        a1  =  Category.objects.get(category_code="A1")
        self.valid_payload = {
            category_id = 1,
            full_description='anorexia nomvorsia',
            abbreviated_description='AM',
            diagnosis_code = 3433,
            code_type = 'ICD-10'
        }

        self.invalid_payload = {
            category_id = 30,
            full_description='anorexia nomvorsia',
            abbreviated_description='AM',
            diagnosis_code = 34,
            code_type = 'ICD-9'

        }

    def test_create_valid_diagnosis(self):
        response = client.post(
            reverse('diagnosisApi:get_diagnosis_detail'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_diagnosis(self):
        response = client.post(
            reverse('diagnosisApi:get_diagnosis_detail'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
