from django.urls import path
from diagnosisApi import views
app_name  =  'diagnosisApi'

urlpatterns  = [
                path('diagnosis/', views.DiagnosisList.as_view(), name="get_diagnosis_list" ) ,
                path('diagnosis/<int:pk>' ,  views.DiagnosisDetail.as_view() , name="get_diagnosis_detail" )

]
