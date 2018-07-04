import json

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

json_reg = {
    "err_code":0,
    "err_meg":"",
}

def regis(request):
    '''
    注册页面
    '''
    username = request.POST['username']
    passwd = request.POST['password']
    
