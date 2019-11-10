import requests
# import os
import json

url = 'https://fcm.googleapis.com/fcm/send'


def send_message(_to, _from, message):
    body = {'to': _to, 'data': {"message": message}}
    body = json.dumps(body).encode('utf8')
    headers = {
        'content-type': 'application/json',
        'Authorization': 'key=' + 'AAAAoaPpcJo:APA91bHMg0Cgj7nkunnr7vxphja5Zetxkk6FjDQ1oB-sHf4YNU8IUyo1o_XDcUOTohKsyf2T061i4Wix4DkDmHJfgYZLebhcgcVhPk25zft8sjOyZlTjGJRuCyuhzpJrkdDtZvseE_P9'
        }
    r = requests.post(url, data=body, headers=headers)
    print(r.text)
