from django.conf.urls import url, include
from django.contrib import admin
from Teacher import views



urlpatterns = [
    url(r'', views.teacher),
]