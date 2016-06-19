from django.conf.urls import url, include
from django.contrib import admin
from Student import views


urlpatterns = [
    url(r'^', views.student),
]