from rest_framework import serializers
from swasthGarbhApp.models import *
from cvd_portal.serializers import DynamicFieldsModelSerializer
from django.contrib.auth.models import User

# class PregenancyPatientsData(DynamicFieldsModelSerializer):

class MedicineSerializer(DynamicFieldsModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all())
    medicines = serializers.SerializerMethodField('get_medicines_data')

    class Meta:
        model = Medicine
        fields = [
            'pk',
            'patient_id',
            'medicines'
        ]

    def get_medicines_data(self, obj):
        qset = Medicine.objects.filter(patient_id=obj.pk)
        ser = MedicinePerPatientSerialzier(qset, many=True, read_only=True)
        return ser.data

class MedicinePerPatientSerialzier(DynamicFieldsModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'pk',
            'medicine_name',
            'medicine_Image'
        ]

class HospitalSerializer(DynamicFieldsModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all())

    class Meta:
        model = Hospital
        fields = [
            'pk',
            'patient_id',
            'xCoordinate',
            'yCoordinate'
        ]

class ComplicationSerializer(DynamicFieldsModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all())

    class Meta:
        model = Complication
        fields = [
            'pk',
            'informationByDoc',
            'patient_id',
            'complicationImage',
            'tookAction',
            'informationByPatient'
        ]

class ComplicationPerPatientSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Complication
        fields = [
            'pk',
            'informationByDoc',
            'complicationImage',
            'tookAction',
            'informationByPatient'
        ]

class PregenancySerializer(DynamicFieldsModelSerializer):

    medicines = serializers.SerializerMethodField('get_medicines_data')
    complications = serializers.SerializerMethodField('get_complications_data')

    class Meta:
        model = PregnancyData
        fields = [
            'pk',
            'patient_id',
            'startDate',
            'medicines',
            'complications',
            'anc1_diabtese',
            'anc1_anemia',
            'anc1_hiv',
            'anc1_ultrasound',
            'anc1_tetnus',
            'anc1_urine',
            'anc2_diabtese',
            'anc2_anemia',
            'anc3_diabtese',
            'anc3_anemia',
            'anc3_urine',
            'anc4_diabtese',
            'anc5_diabtese',
            'anc5_urine',
            'anc6_diabtese',
            'anc6_anemia',
            'anc7_diabtese',
            'anc8_diabtese',
        ]
    def get_medicines_data(self, obj):
        qset = Medicine.objects.filter(patient_id=obj.pk)
        ser = MedicinePerPatientSerialzier(qset, many=True, read_only=True)
        return ser.data
    def get_complications_data(self,obj):
        qset = Complication.objects.filter(patient_id=obj.pk)
        ser = ComplicationPerPatientSerializer(qset, many=True, read_only=True)
        return ser.data
