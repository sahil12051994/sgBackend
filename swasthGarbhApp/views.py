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
import logging
logger = logging.getLogger(__name__)

class All_preg_patients(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = PregnancyData.objects.all()
    serializer_class = PregenancySerializer

class doctor_preg_data(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = PregnancyData.objects.all()
    serializer_class = PregenancySerializer

    def get(self, request, pk):
        patiArr = Patient.objects.filter(doctor=pk).values('id','lmp')
        print("\npat ids: {}\n".format(patiArr))

        d = []
        for patId in patiArr:
            patientId = patId["id"]
            try:
                pregData = PregnancyData.objects.get(patient_id=patientId)
                dataToSend = PregenancySerializer(pregData).data
                d.append(dataToSend)
                print("\n{}\n".format(d))
            except PregnancyData.DoesNotExist:
                pregData = None

        return JsonResponse(
            d,
            safe=False, content_type='application/json')

class Preg_patient_detail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = PregnancyData.objects.all()
    serializer_class = PregenancySerializer

    def get(self, request, pk):
        d = PregnancyData.objects.get(patient_id=pk)
        pDetail = Patient.objects.filter(id=pk).values('lmp')[0]
        dataToSend = PregenancySerializer(d).data
        # print("\ndata prg {}\n".format(dataToSend))
        if(pDetail):
            dataToSend["startDate"] = pDetail['lmp']
        return JsonResponse(
            dataToSend,
            safe=False, content_type='application/json')

    def patch(self, request, *args, **kwargs):
        print(request.body)
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

class particular_medicine(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = MedicinePerPatientSerialzier
    queryset = Medicine.objects.all()

    def get(self, request, pk):
        d = Medicine.objects.get(id=pk)
        return JsonResponse(
            MedicinePerPatientSerialzier(d).data,
            safe=False, content_type='application/json')

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
