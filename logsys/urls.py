from django.conf.urls import patterns,include, url
from logsys import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
#    url(r'^start/', views.start),
]