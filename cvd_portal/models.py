from django.db import models
from django.contrib.auth.models import User
import datetime
from dateutil import tz


class CustomDateTimeField(models.DateTimeField):
    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        to_zone = tz.gettz('Asia/Kolkata')
        return value.astimezone(to_zone)


class Device(models.Model):
    user_type = models.CharField(max_length=20, default="", blank=True)
    device_id = models.TextField()

    def __str__(self):
        return self.device_id


class Doctor(models.Model):
    name = models.CharField(max_length=60, default="Default Doctor")
    hospital = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    mobile = models.IntegerField(blank=True)
    speciality = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    device = models.OneToOneField(Device, null=True, related_name='doctor')
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=60, default="Somesh")
    date_of_birth = models.IntegerField(default=0)
    gender = models.IntegerField(default=1)
    email = models.EmailField(blank=True)
    address = models.TextField(null=True)
    doctor = models.ForeignKey(Doctor, related_name="patients", null=True)
    mobile = models.IntegerField(blank=True)
    device = models.OneToOneField(Device, null=True, related_name='patient')
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    byte = models.TextField()
    patient = models.ForeignKey(Patient, related_name='image')
    time_stamp = CustomDateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.patient.name + ' ' + str(self.time_stamp)


class PatientData(models.Model):
    patient = models.ForeignKey(Patient, related_name='data')
    systolic = models.IntegerField()
    diastolic = models.IntegerField(default=0)
    weight = models.IntegerField()
    heart_rate = models.IntegerField()
    urine_albumin = models.DecimalField(max_digits = 2, decimal_places = 1, default=0)
    headache = models.BooleanField(default=False)
    abdominal_pain = models.BooleanField(default=False)
    visual_problems = models.BooleanField(default=False)
    bleeding_per_vaginum = models.DecimalField(max_digits = 2, decimal_places = 1, default=0)
    decreased_fetal_movements = models.BooleanField(default=False)
    swelling_in_hands_or_face = models.BooleanField(default=False)
    hyper_tension = models.BooleanField(default=False)
    extra_comments = models.TextField(default="")
    time_stamp = CustomDateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.patient.name + ' ' + str(self.time_stamp)


class OTP(models.Model):
    otp = models.IntegerField()
    user_type = models.TextField()
    user_type_id = models.IntegerField()
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return self.user_type + ' ' + str(self.user_id)


class Notifications(models.Model):
    text = models.TextField()
    context_of_notification = models.CharField(max_length=50 , default='None')
    # notification_app = 0 - > Dhandkan
    # notification_app = 1 - > Swasth Garbh
    # notification_app = 2 - > Medicine Reminder
    notification_app = models.PositiveIntegerField(null=True)
    patient = models.ForeignKey(
        Patient, null=True, blank=True)
    doctor = models.ForeignKey(
        Doctor, null=True, blank=True)
    time_stamp = CustomDateTimeField(default=datetime.datetime.now)
    priority = models.PositiveIntegerField(null=True)
    def __str__(self):
        if(self.patient is None):
            return self.doctor.name + " : " + self.text
        else:
            return self.patient.name + " : " + self.text
