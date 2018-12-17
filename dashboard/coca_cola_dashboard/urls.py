from django.conf.urls import url
from coca_cola_dashboard import views

urlpatterns = [
    url(r'^sendsms', views.send_sms),
    url(r'^', views.HomePageView.as_view()),
]