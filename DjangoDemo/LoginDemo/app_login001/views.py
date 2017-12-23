# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
import base64,hashlib

# 引入我们创建的表单类
from .forms import AddForm,FileForm,LoginForm

def index(request):
    return render(request, 'index.html')

def add(request):
    if request.method == 'GET':
        a = request.GET['a']
        b = request.GET['b']
        a = int(a)
        b = int(b)
        print a,b
        return HttpResponse(str(a+b))
    elif request.method == 'POST':
        form = AddForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            file = form.cleaned_data['file_data']
            print file
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
        return HttpResponse(str(int(a) + int(b)))

def upfile(request):
    if request.method == 'POST':
        file = request.FILES['file_data'] # form 包含提交的数据
        print file.name
        with open('./'+file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        print file
        return HttpResponse("ok")

def login(request):
    if request.method == 'POST':
        form = request.POST # form 包含提交的数据

        a = form['login_password']
        b = form['login_username']
        return HttpResponse()