import datetime
from cvd_portal.fcm import send_message
from cvd_portal.models import Patient, PatientData, Notifications
from swasthGarbhApp.models import PregnancyData
from swasthGarbhApp.models import *

def generate_message(preg_data,patient_data,patient,preg_patient_details):
    gen_msg = False
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
            message += '  Facing Visual Problems'
        if ( preg_data['bleeding_per_vaginum'] == True ):
            message += '  Bleeding Vaginum'
        if ( preg_data['decreased_fetal_movements'] == True ):
            message += 'Decreased Fetal Movements'
        if ( preg_data['swelling_in_hands_or_face'] == True ):
            message += '  Swelling in hands & face'
        message = message + ""
        return message

def check_who_following(request, pk):
    who_following = 0;
    pd = PregnancyData.objects.filter(patient_id= pk).values(
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
        'anc8_diabtese').first()

    print("In Who Check patient id: {}".format(pk))
    if(pd):
        if(pd['anc1_diabtese'] &  pd['anc1_anemia'] & pd['anc1_hiv'] & pd['anc1_ultrasound'] & pd['anc1_tetnus'] & pd['anc1_urine']):
            who_following = who_following + 1;
        if (pd['anc2_diabtese'] &  pd['anc2_anemia']):
            who_following = who_following + 1;
        if (pd['anc3_diabtese'] &  pd['anc3_anemia'] & pd['anc3_urine']):
            who_following = who_following + 1;
        if (pd['anc4_diabtese']):
            who_following = who_following + 1;
        if (pd['anc5_diabtese'] &  pd['anc5_urine']):
            who_following = who_following + 1;
        if (pd['anc6_diabtese'] &  pd['anc6_anemia']):
            who_following = who_following + 1;
        if (pd['anc7_diabtese']):
            who_following = who_following + 1;
        if (pd['anc8_diabtese']):
            who_following = who_following + 1;
    return who_following

def get_doctor_patients(request,pk):
    doc = Patient.objects.filter(doctor=pk).values_list('id')
    res_list = [x[0] for x in doc]
    print(res_list)
    numberOfPatientFollowingWHO = 0
    analysis_obj = {}
    analysis_obj['high_sys'] = 0
    analysis_obj['high_dys'] = 0
    analysis_obj['high_weight'] = 0
    analysis_obj['hyper_tension'] = 0
    analysis_obj['urine_albumin'] = 0

    for patientId in res_list:
        particular_pat = PatientData.objects.filter(patient = patientId).order_by('-time_stamp').values(
        'systolic',
        'diastolic',
        'weight',
        'urine_albumin',
        'hyper_tension',
        'patient'
        ).first()
        print(particular_pat)
        if(particular_pat):
            if (particular_pat['systolic'] > 80):
                analysis_obj['high_sys'] = analysis_obj['high_sys'] + 1
            if (particular_pat['diastolic'] > 140):
                analysis_obj['high_dys'] = analysis_obj['high_dys'] + 1
            if (particular_pat['weight'] > 80):
                analysis_obj['high_weight'] = analysis_obj['high_weight'] + 1
            if (particular_pat['urine_albumin'] > 2):
                analysis_obj['urine_albumin'] = analysis_obj['urine_albumin'] + 1
            if (particular_pat['hyper_tension'] == True):
                analysis_obj['hyper_tension'] = analysis_obj['hyper_tension'] + 1
        if(check_who_following(request,patientId) > 0):
            numberOfPatientFollowingWHO = numberOfPatientFollowingWHO + 1;

    analysis_obj['who_following'] = numberOfPatientFollowingWHO
    print(analysis_obj)
    return analysis_obj

def check_for_preeclampsia_in_current(request):
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
