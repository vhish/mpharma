from rest_framework import serializers

from diagnosisApi.models import Diagnosis, Category

class DiagnosisSerializer(serializers.ModelSerializer):
    full_code = serializers.SerializerMethodField()

    def get_full_code(self, obj):
        return obj.category.category_code + str(obj.diagnosis_code)

    class Meta:
        model = Diagnosis
        fields = ('diagnosis_code' ,  'abbreviated_description' ,  'full_description' , 'category', 'full_code', 'code_type' )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_code', 'category_title')
