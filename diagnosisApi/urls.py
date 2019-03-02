from django.urls import path
from diagnosisApi import views
app_name  =  'diagnosisApi'

urlpatterns  = [
                path('diagnosis/', views.DiagnosisList.as_view() ) ,
                path('diagnosis/<int:pk>' ,  views.DiagnosisDetail.as_view() )

]
