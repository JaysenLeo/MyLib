# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from django.http import StreamingHttpResponse
from .models import PackageAuth,PackageMain
# Create your views here.

import datetime
import json
from hashlib import md5
from form_analyze import RouterForm,AuthForm,DownloadForm


def server(request):
    pass

def router_handle(request):
    package_token = None
    p_token = None
    run = None
    if request.method == 'POST':
        router_form = RouterForm(request.POST)
        if router_form.is_valid():# 如果提交的数据合法
            router = router_form.cleaned_data['router']
            username = router_form.cleaned_data['username']
            token = router_form.cleaned_data['token']

            try:
                package_token = PackageAuth.objects.filter(p_username=username).values('p_token')
            except Exception as e:

                HttpResponse(json.dumps(
                    {
                        'auth_msg':
                         {
                             'msg_category': 'Error',
                             'msg_body': 'Wrong usename'
                         }
                    }
            ))
            p_token = package_token[0]['p_token']
            if p_token != token:
                HttpResponse(json.dumps(
                    {
                        'auth_msg':
                         {
                             'msg_category': 'Error',
                             'msg_body': 'Wrong token'
                         }
                    }
            ))
            if router == 'WebServer':
                from handle_api.WebServer import run
                return run(request)
    return HttpResponse(json.dumps({'':''}))

def index(request):

    return render(request, 'index.html')

def login(request):
    token = None
    username = None
    password = None
    package_auth = None
    if request.method == 'POST':
        auth_form = AuthForm(request.POST) # form 包含提交的数据
        if auth_form.is_valid():# 如果提交的数据合法
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']

        # 认证
        try:
            package_auth = PackageAuth.objects.filter(p_username=username).values('p_token', 'p_password')
        except Exception as e:
            return HttpResponse(json.dumps(
                    {
                        'auth_msg':
                         {
                             'msg_category': 'Error',
                             'msg_body': 'Wrong username'
                         }
                    }
            ))
        if len(package_auth) == 0:
            return HttpResponse(json.dumps(
                    {
                        'auth_msg':
                         {
                             'msg_category': 'Fail',
                             'msg_body': 'User Name does not exist'
                         }
                    }
            ))

        if package_auth[0]['p_password'] != password:
            return HttpResponse(json.dumps(
                    {
                        'auth_msg':
                            {
                                'msg_category': 'Error',
                                'msg_body': 'Wrong password'
                            }
                    }
            ))
        token = md5(str(datetime.datetime.now())+username+'package_man').hexdigest()
        PackageAuth.objects.filter(p_username=username).update(p_token=token)

        return HttpResponse(json.dumps(
            {
                'auth_msg':
                 {
                     'msg_category': 'Successful',
                     'msg_body': {
                         'token': token,
                     }
                 }
            }
        ))
    return HttpResponse(json.dumps(
            {
                'auth_msg':
                 {
                     'msg_category': 'Fail',
                     'msg_body': 'Login Fail!!!'
                 }
            }
        ))
    #     token = request.GET['token']
    #
    #     router = request.GET['router']
    #     category = request.GET['category']
    #     category = request.GET['category']
    #     if router == '':
    #         pass
    # if request.method == 'GET':
    #
    #
    #         pass
    #




