# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
from dateutil import tz
from cvd_portal.models import *

class PregnancyData(models.Model):

    patient_id = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    startDate = CustomDateTimeField(default=datetime.datetime.now)

    anc1_diabtese = models.BooleanField(default=0)
    anc1_anemia = models.BooleanField(default=0)
    anc1_hiv = models.BooleanField(default=0)
    anc1_ultrasound = models.BooleanField(default=0)
    anc1_tetnus = models.BooleanField(default=0)
    anc1_urine = models.BooleanField(default=0)
    anc1_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc1_safeDate = CustomDateTimeField(default=datetime.datetime.now)

    anc2_diabtese = models.BooleanField(default=0)
    anc2_anemia = models.BooleanField(default=0)
    anc2_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc2_safeDate = CustomDateTimeField(default=datetime.datetime.now)

    anc3_diabtese = models.BooleanField(default=0)
    anc3_anemia = models.BooleanField(default=0)
    anc3_urine = models.BooleanField(default=0)
    anc3_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc3_safeDate = CustomDateTimeField(default=datetime.datetime.now)

    anc4_diabtese = models.BooleanField(default=0)
    anc4_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc4_safeDate = CustomDateTimeField(default=datetime.datetime.now)

    anc5_diabtese = models.BooleanField(default=0)
    anc5_urine = models.BooleanField(default=0)
    anc5_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc5_safeDate = CustomDateTimeField(default=datetime.datetime.now)

    anc6_diabtese = models.BooleanField(default=0)
    anc6_anemia = models.BooleanField(default=0)
    anc6_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc6_safeDate = CustomDateTimeField(default=datetime.datetime.now)

    anc7_diabtese = models.BooleanField(default=0)
    anc7_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc7_safeDate = CustomDateTimeField(default=datetime.datetime.now)

    anc8_diabtese = models.BooleanField(default=0)
    anc8_dueDate = CustomDateTimeField(default=datetime.datetime.now)
    anc8_safeDate = CustomDateTimeField(default=datetime.datetime.now)

    time_stamp = CustomDateTimeField(default=datetime.datetime.now)

class Medicine(models.Model):
    patient_id = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        null=True
    )
    medicine_name = models.CharField(max_length=50)
    medicine_freq = models.CharField(max_length=50, default="")
    medicine_Image = models.TextField(default="")
    medicine_extra_comments = models.TextField(default="")
    medicine_start = CustomDateTimeField(default=datetime.datetime.now)
    medicine_end = CustomDateTimeField(default=datetime.datetime.now)
    isSOS = models.BooleanField(default=False)

class Hospital(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patientsPregHospitals')
    xCoordinate = models.DecimalField(max_digits = 20, decimal_places = 15)
    yCoordinate = models.DecimalField(max_digits = 20, decimal_places = 15)

class Complication(models.Model):
    informationByDoc = models.TextField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patientsComplication')
    complicationImage = models.TextField()
    tookAction = models.BooleanField(default=0)
    informationByPatient = models.TextField()
