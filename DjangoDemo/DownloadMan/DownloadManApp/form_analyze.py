# _*_coding:utf-8_*_
from django import forms

class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class DownloadForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class RouterForm(forms.Form):
    router = forms.CharField()
    token = forms.CharField()
    category = forms.CharField()
    version = forms.CharField()
    type = forms.CharField()
    username = forms.CharField()
    method = forms.CharField()
    filename = forms.CharField()


