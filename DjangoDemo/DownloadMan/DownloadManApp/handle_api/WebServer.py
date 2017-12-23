# _*_coding:utf-8_*_


from ..form_analyze import RouterForm
from ..models import PackageAuth,PackageMain
from django.http import StreamingHttpResponse
from django.shortcuts import render,HttpResponse
import os

def run(request):
    category = None
    version = None
    type = None
    username = None
    response = None
    if request.method == 'POST':
        router_form = RouterForm(request.POST)
        if router_form.is_valid():# 如果提交的数据合法
            category = router_form.cleaned_data['category']
            version = router_form.cleaned_data['version']
            type = router_form.cleaned_data['type']
            username = router_form.cleaned_data['username']
            filename = router_form.cleaned_data['filename']
            method = router_form.cleaned_data['method']
            down_url = PackageMain.objects.filter(p_name=filename).values('p_local_downloads')[0]['p_local_downloads']
            from BigFileIterator import big_file_download
            print os.path.join(down_url,filename)
            response = StreamingHttpResponse(big_file_download(os.path.join(down_url,filename)))
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
        return response





