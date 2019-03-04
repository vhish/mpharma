from django.urls import path
from diagnosisApi import views
app_name  =  'diagnosisApi'

urlpatterns  = [
                path('diagnosis/', views.DiagnosisList.as_view(), name="get_diagnosis_list" ) ,
                path('diagnosis/<int:pk>' ,  views.DiagnosisDetail.as_view() , name="get_diagnosis_detail" ),
                #path('category/', views.CategoryList.as_view(), name="get_category_list" ),
                #path('category/<int:pk>' ,  views.CategoryDetail.as_view() , name="get_category_detail" )
            ]
