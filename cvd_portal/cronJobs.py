import requests
import os
import json
from datetime import date

from cvd_portal.models import *
from swasthGarbhApp.models import PregnancyData

url = 'https://fcm.googleapis.com/fcm/send'

def checkNotificationPending() :

    for patient in PregnancyData.objects.all() :
        try :
            print(patient)
            print(patient.patient_id.id)

            anc1_dueDate = (date.today() - patient.anc1_dueDate.date()).days
            anc2_dueDate = (date.today() - patient.anc2_dueDate.date()).days
            anc3_dueDate = (date.today() - patient.anc3_dueDate.date()).days
            anc4_dueDate = (date.today() - patient.anc4_dueDate.date()).days
            anc5_dueDate = (date.today() - patient.anc5_dueDate.date()).days
            anc6_dueDate = (date.today() - patient.anc6_dueDate.date()).days
            anc7_dueDate = (date.today() - patient.anc7_dueDate.date()).days
            anc8_dueDate = (date.today() - patient.anc8_dueDate.date()).days

            l_date = date.today()

            print(
            "datesssss",
            anc1_dueDate,
            anc2_dueDate,
            anc3_dueDate,
            anc4_dueDate,
            anc5_dueDate,
            anc6_dueDate,
            anc7_dueDate,
            anc8_dueDate
            )
            notifMessage = ''
            send_message = 0

            if(anc1_dueDate == 0) :
                notifMessage = 'Your ANC1 Date today'
                send_message = 1
            if(anc1_dueDate == 2) :
                notifMessage = 'Your ANC1 Date after 2 days'
                send_message = 1
            if(anc1_dueDate == -5) :
                notifMessage = 'Your ANC1 Date has Past, Please Visit'
                send_message = 1


            if(anc2_dueDate == 0) :
                notifMessage = 'Your AN2 Date today'
                send_message = 1
            if(anc2_dueDate == 2) :
                notifMessage = 'Your ANC2 Date after 2 days'
                send_message = 1
            if(anc2_dueDate == -5) :
                notifMessage = 'Your ANC2 Date has Past, Please Visit'
                send_message = 1

            if(anc3_dueDate == 0) :
                notifMessage = 'Your ANC3 Date today'
                send_message = 1
            if(anc3_dueDate == 2) :
                notifMessage = 'Your ANC3 Date after 2 days'
                send_message = 1
            if(anc3_dueDate == -5) :
                notifMessage = 'Your ANC3 Date has Past, Please Visit'
                send_message = 1


            if(anc4_dueDate == 0) :
                notifMessage = 'Your ANC4 Date today'
                send_message = 1
            if(anc4_dueDate == 2) :
                notifMessage = 'Your ANC4 Date after 2 days'
                send_message = 1
            if(anc4_dueDate == -5) :
                notifMessage = 'Your ANC4 Date has Past, Please Visit'
                send_message = 1


            if(anc5_dueDate == 0) :
                notifMessage = 'Your ANC5 Date today'
                send_message = 1
            if(anc5_dueDate == 2) :
                notifMessage = 'Your ANC5 Date after 2 days'
                send_message = 1
            if(anc5_dueDate == -5) :
                notifMessage = 'Your ANC5 Date has Past, Please Visit'
                send_message = 1


            if(anc6_dueDate == 0) :
                notifMessage = 'Your ANC6 Date today'
                send_message = 1
            if(anc6_dueDate == 2) :
                notifMessage = 'Your ANC6 Date after 2 days'
                send_message = 1
            if(anc6_dueDate == -5) :
                notifMessage = 'Your ANC6 Date has Past, Please Visit'
                send_message = 1

            if(anc7_dueDate == 0) :
                notifMessage = 'Your ANC7 Date today'
                send_message = 1
            if(anc7_dueDate == 2) :
                notifMessage = 'Your ANC7 Date after 2 days'
                send_message = 1
            if(anc7_dueDate == -5) :
                notifMessage = 'Your ANC7 Date has Past, Please Visit'
                send_message = 1


            if(anc8_dueDate == 0) :
                notifMessage = 'Your ANC8 Date today'
                send_message = 1
            if(anc8_dueDate == 2) :
                notifMessage = 'Your ANC8 Date after 2 days'
                send_message = 1
            if(anc8_dueDate == -5) :
                notifMessage = 'Your ANC8 Date has Past, Please Visit'
                send_message = 1

            if(send_message == 1) :
                _to = patient.patient_id.device.device_id
                message = notifMessage
                body = {'to': _to, 'data': {"message": message}}
                body = json.dumps(body).encode('utf8')
                headers = {
                    'content-type': 'application/json',
                    'Authorization': 'key=' + 'AAAAoaPpcJo:APA91bHMg0Cgj7nkunnr7vxphja5Zetxkk6FjDQ1oB-sHf4YNU8IUyo1o_XDcUOTohKsyf2T061i4Wix4DkDmHJfgYZLebhcgcVhPk25zft8sjOyZlTjGJRuCyuhzpJrkdDtZvseE_P9'
                    }
                r = requests.post(url, data=body, headers=headers)

        except Exception as e: print(e)
