from django.conf.urls import url, include
from rest_framework.authtoken import views
from cvd_portal.views import *

app_name = 'cvd_portal'

urlpatterns = [
    url(r'api/patient/(?P<pk>[0-9]+)$', PatientDetail.as_view()),
    url(r'api/patient$', PatientList.as_view()),
    url(r'api/doctor/(?P<pk>[0-9]+)$', DoctorDetail.as_view()),
    url(r'api/doctor$', DoctorList.as_view()),
    # url(r'api/user$', UserCreate.as_view()),
    url(r'api/user/(?P<pk>[0-9]+)$', UserDestroy.as_view()),
    url(r'api/data/(?P<pk>[0-9]+)$', PatientDataDetail.as_view()),
    url(r'api/data$', PatientDataCreate.as_view()),
    url(r'api/image/(?P<pk>[0-9]+)$', PatientImageDetail.as_view()),
    url(r'api/allimages/(?P<pk>[0-9]+)$', PatientAllImagesDetail.as_view()),
    url(r'api/singleimage/(?P<pk>[0-9]+)$', ParticularImageByte.as_view()),
    url(r'api/image$', PatientImageCreate.as_view()),
    url(r'api/login$', Login.as_view()),
    url(r'api/logout$', Logout.as_view()),
    url(r'api/onboard/doc$', DocOnboarding.as_view()),
    url(r'api/onboard/patient$', PatientOnboarding.as_view()),
    url(r'api/device$', DeviceCRUD.as_view()),
    url(r'api/resultsByDoc/(?P<pk>[0-9]+)$', ResultsByDoc.as_view()),
    url(r'api/trimesterNotify$', trimesterNotify.as_view()),

    # NOTIFICATION API
    url(r'api/notification$', NotificationCRUD.as_view()),
    url(
        r'api/notification/patient/(?P<pk>[0-9]+)$',
        patient_notification.as_view()),
    url(
        r'api/notification/doctor/(?P<pk>[0-9]+)$',
        doctor_notification.as_view()),


    url(r'api/gen_otp$', gen_otp.as_view()),
    url(r'api/verify_otp$', verify_otp.as_view()),
    url(r'swasthgarbh/',include('swasthGarbhApp.urls')),
    url(r'chikitsa/',include('medicine_reminder.urls')),
]
