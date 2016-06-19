from django import forms
from django.http import HttpResponse



class login(forms.Form):
    login = forms.CharField()
    password = forms.CharField()

    template = loa