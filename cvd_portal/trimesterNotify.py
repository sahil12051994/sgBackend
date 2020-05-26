import requests
import os
import json
from datetime import date

from cvd_portal.models import *

url = 'https://fcm.googleapis.com/fcm/send'

def trimesterNotifyFunc(data) :
    print("Inside Function: ", data)
    for patient in Patient.objects.all() :
        try :

            # doctor = Doctor.objects.get(patient.doctor)
            if(patient.doctor and data['doctorId'] == patient.doctor.pk):

                lmpDate = (date.today() - patient.lmp.date()).days

                notifMessage = ''
                send_message = 0

                if(lmpDate <= 90) :
                    notifMessage = data['trimesterOneText']
                    send_message = 1
                elif (lmpDate > 90 and lmpDate <= 180) :
                    notifMessage = data['trimesterTwoText']
                    send_message = 1
                elif(lmpDate > 180 and lmpDate <= 300) :
                    notifMessage = data['trimesterThreeText']
                    send_message = 1

                print("Patient Name: ", patient, "Doctor Id: ", patient.doctor.pk, "Phone Id: ", patient.device.device_id ,"LMP Date: ", patient.lmp, "Days Past from LMP: ", lmpDate, "Message: ", notifMessage)

                if(send_message == 1) :
                    Notifications(text=notifMessage, patient=patient).save()
                    Notifications(text="Patient " + patient.name +  " was advised for Trimester : " + notifMessage, doctor=patient.doctor).save()
                    _to = patient.device.device_id
                    message = notifMessage
                    body = {'to': _to, 'data': {"message": message}}
                    body = json.dumps(body).encode('utf8')
                    headers = {
                        'content-type': 'application/json',
                        'Authorization': 'key=' + 'AAAAoaPpcJo:APA91bHMg0Cgj7nkunnr7vxphja5Zetxkk6FjDQ1oB-sHf4YNU8IUyo1o_XDcUOTohKsyf2T061i4Wix4DkDmHJfgYZLebhcgcVhPk25zft8sjOyZlTjGJRuCyuhzpJrkdDtZvseE_P9'
                        }
                    r = requests.post(url, data=body, headers=headers)

        except Exception as e: print(e)

    result = {"status": "ok"}
    return result
