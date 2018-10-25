# -*- coding: utf-8 -*-
from cvd_portal.models import Patient
from swasthGarbhApp.models import *
from swasthGarbhApp.serializers import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse

from rest_framework.exceptions import ParseError
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from cvd_portal.fcm import send_message
from swasthGarbhApp.logic import *
from random import randint

class All_preg_patients(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = PregnancyData.objects.all()
    serializer_class = PregenancySerializer

class Preg_patient_detail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = PregnancyData.objects.all()
    serializer_class = PregenancySerializer

    def get(self, request, pk):
        d = PregnancyData.objects.get(patient_id=pk)
        return JsonResponse(
            PregenancySerializer(d).data,
            safe=False, content_type='application/json')

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class Medicine_particular_patient_detail(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MedicinePerPatientSerialzier

    def get(self, request, pk):
        d = Medicine.objects.filter(patient_id=pk)
        return JsonResponse(
            MedicinePerPatientSerialzier(d,many=True).data,
            safe=False, content_type='application/json')

    def post(self, request, *args, **kwargs):
        return super().post(request)

class Hospital_detail(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class Pregnancy_data_create(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = PregenancySerializer

    def post(self, request):
        check_for_preeclampsia_in_current(request)
        return super(Pregnancy_data_create , self).post(request)
