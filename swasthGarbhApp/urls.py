from django.conf.urls import *
from rest_framework.authtoken import views
from swasthGarbhApp.views import *

app_name = 'swasthGarbhApp'

urlpatterns = [
    url(r'patient/(?P<pk>[0-9]+)$', Preg_patient_detail.as_view()),
    url(r'patient$', All_preg_patients.as_view()),
    url(r'doc/(?P<pk>[0-9]+)$', doctor_preg_data.as_view()),
    url(r'patient/(?P<pk>[0-9]+)/med$', Medicine_particular_patient_detail.as_view()),
    url(r'med/(?P<pk>[0-9]+)$', particular_medicine.as_view()),
    url(r'hospital$', Hospital_detail.as_view()),
    url(r'patient/pregDataAdd',Pregnancy_data_create.as_view()),
]
