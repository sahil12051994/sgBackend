
################################################################################
GET ALL PATIENTS DETAILS
url(r'patient$', All_preg_patients.as_view())

Request:
curl -X GET \
  http://localhost:8000/cbtbiitr/swasthgarbh/patient/ \
  -H 'authorization: Token 33c5f694679413429efd51154880bd667f26d8c5' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \

Output :
[{"pk":1,"patient_id":1,"startDate":"2018-06-20T17:44:14+05:30","medicines":[{"pk":1,"medicine_name":"Pregnancy Medicine 1","medicine_Image":"Image file for medicine"},{"pk":2,"medicine_name":"Pregnancy Medicine 2","medicine_Image":"93420-9812-9318293417-03412"}],"complications":[{"pk":1,"informationByDoc":"Complication information by doctor","complicationImage":"complication image by patient","tookAction":true,"informationByPatient":"complication information byb patient"}],"anc1":[{"pk":1,"diabtese":true,"anemia":false,"hiv":false,"ultrasound":true,"tetnus":false,"urine":true}],"anc2":[{"pk":1,"diabtese":true,"anemia":true}],"anc3":[{"pk":1,"diabtese":true,"anemia":false,"urine":false}],"anc4":[{"pk":1,"diabtese":true}],"anc5":[{"pk":1,"diabtese":false,"urine":true}],"anc6":[{"pk":2,"diabtese":false,"anemia":true}],"anc7":[{"pk":1,"diabtese":true}],"anc8":[{"pk":1,"diabtese":true}]},{"pk":2,"patient_id":2,"startDate":"2018-06-13T18:38:42+05:30","medicines":[{"pk":3,"medicine_name":"Pregnancy Medicine 3","medicine_Image":"sadascfas"}],"complications":[],"anc1":[],"anc2":[],"anc3":[],"anc4":[],"anc5":[],"anc6":[],"anc7":[],"anc8":[]},{"pk":3,"patient_id":3,"startDate":"2018-06-03T18:39:03+05:30","medicines":[{"pk":4,"medicine_name":"Pregnancy Medicine 4","medicine_Image":"adscfadcfadcfds"}],"complications":[],"anc1":[],"anc2":[],"anc3":[],"anc4":[],"anc5":[],"anc6":[],"anc7":[],"anc8":[]}]
################################################################################
################################################################################
################################################################################
################################################################################
GET PARTICULAR PATIENT DETAILS
url(r'patient/(?P<pk>[0-9]+)$', Preg_patient_detail.as_view())

Request:
curl -X GET \
  http://localhost:8000/cbtbiitr/swasthgarbh/patient/1 \
  -H 'authorization: Token 33c5f694679413429efd51154880bd667f26d8c5' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \

Output :
{"pk":1,"patient_id":1,"startDate":"2018-06-20T17:44:14+05:30","medicines":[{"pk":1,"medicine_name":"Pregnancy Medicine 1","medicine_Image":"Image file for medicine"},{"pk":2,"medicine_name":"Pregnancy Medicine 2","medicine_Image":"93420-9812-9318293417-03412"}],"complications":[{"pk":1,"informationByDoc":"Complication information by doctor","complicationImage":"complication image by patient","tookAction":true,"informationByPatient":"complication information byb patient"}],"anc1":[{"pk":1,"diabtese":true,"anemia":false,"hiv":false,"ultrasound":true,"tetnus":false,"urine":true}],"anc2":[{"pk":1,"diabtese":true,"anemia":true}],"anc3":[{"pk":1,"diabtese":true,"anemia":false,"urine":false}],"anc4":[{"pk":1,"diabtese":true}],"anc5":[{"pk":1,"diabtese":false,"urine":true}],"anc6":[{"pk":2,"diabtese":false,"anemia":true}],"anc7":[{"pk":1,"diabtese":true}],"anc8":[{"pk":1,"diabtese":true}]}
################################################################################
################################################################################
################################################################################
################################################################################
GET PARTICULAR PATIENT MEDICINE DETAILS
url(r'patient/(?P<pk>[0-9]+)/med$', Medicine_particular_patient_detail.as_view()),

Request:
curl -X GET \
  http://localhost:8000/cbtbiitr/swasthgarbh/patient/1/med \
  -H 'authorization: Token 33c5f694679413429efd51154880bd667f26d8c5' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \

Output :
{"pk":1,"patient_id":1,"medicines":[{"pk":1,"medicine_name":"Pregnancy Medicine 1","medicine_Image":"Image file for medicine"},{"pk":2,"medicine_name":"Pregnancy Medicine 2","medicine_Image":"93420-9812-9318293417-03412"}]}
################################################################################
################################################################################
################################################################################
################################################################################
GET ALL HOSPITAL DETAILS
url(r'hospital$', Hospital_detail.as_view()),

Request:
curl -X GET \
  http://localhost:8000/cbtbiitr/swasthgarbh/hospital \
  -H 'authorization: Token 33c5f694679413429efd51154880bd667f26d8c5' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \

Output :
[{"pk":1,"patient_id":1,"xCoordinate":"4.2340","yCoordinate":"3.3430"},{"pk":2,"patient_id":1,"xCoordinate":"3.2340","yCoordinate":"4.3420"},{"pk":3,"patient_id":2,"xCoordinate":"4.3450","yCoordinate":"6.2340"},{"pk":4,"patient_id":3,"xCoordinate":"5.2340","yCoordinate":"1.2340"}]################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
GET ALL Pregnancy data DETAILS
url(r'patient/allPregData',Pregnancy_data_read.as_view())

Request:
curl -X GET \
  http://localhost:8000/cbtbiitr/swasthgarbh/patient/allPregData \
  -H 'authorization: Token 33c5f694679413429efd51154880bd667f26d8c5' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \

Output :
[{"pk":2,"patient_id":1,"urine_albumin":"2.3","headache":true,"abdominal_pain":true,"visual_problems":false,"bleeding_per_vaginum":false,"decreased_fetal_movements":true,"swelling_in_hands_or_face":true,"time_stamp":"2018-06-20T23:32:10+05:30"},{"pk":3,"patient_id":2,"urine_albumin":"2.4","headache":false,"abdominal_pain":false,"visual_problems":false,"bleeding_per_vaginum":true,"decreased_fetal_movements":true,"swelling_in_hands_or_face":true,"time_stamp":"2018-06-12T23:32:19+05:30"},{"pk":4,"patient_id":1,"urine_albumin":"2.1","headache":true,"abdominal_pain":false,"visual_problems":false,"bleeding_per_vaginum":false,"decreased_fetal_movements":false,"swelling_in_hands_or_face":false,"time_stamp":"2018-06-20T23:32:35+05:30"},{"pk":5,"patient_id":2,"urine_albumin":"2.4","headache":false,"abdominal_pain":false,"visual_problems":false,"bleeding_per_vaginum":true,"decreased_fetal_movements":true,"swelling_in_hands_or_face":true,"time_stamp":"2018-06-20T23:38:44.292630+05:30"}]
################################################################################
################################################################################
################################################################################
################################################################################
ADD Pregnancy data DETAILS
url(r'patient/pregDataAdd',Pregnancy_data_create.as_view()),

Request:
curl -X POST \
  http://localhost:8000/cbtbiitr/swasthgarbh/patient/pregDataAdd \
  -H 'authorization: Token 33c5f694679413429efd51154880bd667f26d8c5' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 27081598-9c59-68b0-2f9a-7ceeac85aadb' \
  -d '{
		    "patient_id": 2,
        "urine_albumin": "2.4",
        "headache": "false",
        "abdominal_pain": "false",
        "visual_problems": "false",
        "bleeding_per_vaginum": "true",
        "decreased_fetal_movements": "true",
        "swelling_in_hands_or_face": "true"
        }'

Output :
{"pk":6,"patient_id":2,"urine_albumin":"2.4","headache":false,"abdominal_pain":false,"visual_problems":false,"bleeding_per_vaginum":true,"decreased_fetal_movements":true,"swelling_in_hands_or_face":true,"time_stamp":"2018-06-20T23:45:05.953002"}
