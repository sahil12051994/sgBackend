import datetime
from cvd_portal.fcm import send_message
from cvd_portal.models import Patient, PatientData, Notifications
from swasthGarbhApp.models import *

def generate_message(preg_data,patient_data,patient,preg_patient_details):
    gen_msg = False
    # number_of_weeks = datetime.datetime.now() - preg_patient_details.startDate
    # number_of_weeks = number_of_weeks.days
    for key in preg_data:
        if(preg_data[key] == True):
            gen_msg = True
    if gen_msg is False:
        return None
    else:
        # message = "Patient named '" + patient.name + "' with '"+ number_of_weeks +"'weeks of pregnancy suffered symptoms showing"
        if ( preg_data['urine_albumin'] > 2 ) :
            message += ' Urine albumin level is high'
        if ( preg_data['headache'] == True ) :
            message += '  Severe Headache'
        if ( preg_data['abdominal_pain'] == True ):
            message += '  Abdominal Pain'
        if ( preg_data['visual_problems'] == True ):
            message += '  facing Visual Problems'
        if ( preg_data['bleeding_per_vaginum'] == True ):
            message += '  Bleeding Vaginum'
        if ( preg_data['decreased_fetal_movements'] == True ):
            message += '  with Decreased Fetal Movements'
        if ( preg_data['swelling_in_hands_or_face'] == True ):
            message += '  Swelling in hands & face'
        message = message + ""
        return message

def check_for_preeclampsia_in_current(request):
    #BP > 150/110
    #BP >140/90 + Urine Albumin > 2
    #if headache == true
    #if abdominal_pain == true
    #if visual_problems == true
    #if bleeding_per_vaginum == true
    #if decreased_fetal_movements == true
    #if swelling_in_hands_or_face == true

    # preg_data = PregnancyData.objects.get(pk = request.data['pk'])
    preg_data = request.data
    patient = Patient.objects.get(pk = request.data['patient_id'])
    patient_data = PatientData.objects.filter(patient = request.data['patient_id']).filter(time_stamp = request.data['time_stamp'])
    preg_patient_details = Pregenancy.objects.get(patient_id = request.data['patient_id'])
    doc_message = generate_message(preg_data , patient_data ,  patient , preg_patient_details)
    print("lalalalalala \n\n {}".format(doc_message))
    if(doc_message is None):
        return
    else:
        doc_device_id = p.doctor.device.device_id
        patient_device_id = p.device.device_id
        send_message(doc_device_id, None, doc_message)
        patient_message = "Please visit your doctor"
        send_message(patient_device_id, None, patient_message)
        Notifications(text=doc_message, doctor=patient.doctor).save()
        Notifications(text=patient_message, patient=patient).save()
