
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import User
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import *
import time
import json
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt




def regist(request):
    err_code=0
    err_msg=[]
    if request.method=='POST':
        obj=RegisterForm(request.POST)
        if obj.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            User.objects.create(username=username, password=password)

            res={"err_code":0}
            return HttpResponse(json.dumps(res))

        else:
            errors=obj.errors

            res = {"err_code": 1,"err_msg":errors}
            return HttpResponse(json.dumps(res))

    else:

        return HttpResponse('fail!')



def login(request):
    if request.method=='POST':
        obj=LoginForm(request.POST)
        if obj.is_valid():
            data=obj.cleaned_data
            username = request.POST['username']
            password = request.POST['password']

            User = auth.authenticate(username=username, password=password)

            now_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            request.session['last_login_time']=now_time  #用户的上一次登录时间


            ip = request.META['REMOTE_ADDR']
            request.session['last_login_ip']=ip #用户的上一次登录ip

            request.session['is_login']=True  #用户已经登录的状态
            request.session['user']=username  #用户名
            request.session.set_expiry(3600)  #session过期时间

            res = {"err_code": 0}

            return HttpResponse(json.dumps(res))
        else:
            errors = obj.errors

            res = {"err_code": 1, "err_msg": errors}
            return HttpResponse(json.dumps(res))

def profile(request):

    if request.session.get('is_login',None):
        res={'err_code':0,'err_msg':'','username':request.session.get('user',None),'last_login_time':request.session.get("last_login_time",None),
             'last_login_ip':request.session.get('last_login_ip',None)}
        return HttpResponse(json.dumps(res),content_type="application/json")
    else:
        res = {'err_code':1, 'err_msg': 'did not login'}
        return HttpResponse(json.dumps(res),content_type="application/json")

def logout(request):

    auth.logout(request)
    del request.session['is_login']
    del request.session['user']

    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    request.session['last_logout_time'] = now_time  # 用户的上一次登出时间

    ip = request.META['REMOTE_ADDR']
    request.session['last_logout_ip'] = ip  # 用户的上一次登出ip

    res = {'err_code': 0, 'err_msg':''}
    return HttpResponse(json.dumps(res),content_type="application/json")

def image(request):

    n=int(request.GET['n'])

    x=[]
    y=[]
    for i in range(0,n+1):
        global string
        string=('x'+str(i))

        try:
            x.append(request.GET[string])
            y.append(request.GET[string])
        except:
            pass

    plt.plot(x,y)
    plt.savefig("logsystem/static/images/picture"+str(n)+'.jpg')
    img=open("logsystem/static/images/picture"+str(n)+'.jpg','rb')
    return HttpResponse(img,content_type="image/jpg")

