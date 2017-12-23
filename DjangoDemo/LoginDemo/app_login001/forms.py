# _*_coding:utf-8_*_
from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()

class FileForm(forms.Form):
    file_data = forms.CharField

class LoginForm(forms.Form):
    user = forms.CharField()
    pwd = forms.CharField()