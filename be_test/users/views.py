import json
import datetime
import numpy as np
import matplotlib.pyplot as plt
import os

from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from users.models import Users 

# Create your views here.

json_reg = {
    "err_code":0,
    "err_msg":"",
}

def regis_view(request):
    '''
    注册页面
    '''
    username = request.POST['username']
    password = request.POST['password']

    ret = json_reg.copy()

    if len(username) > 30:
        ret["err_code"] = -1,
        ret["err_msg"] = "Username is too long."
    elif len(password) > 50:
        ret["err_code"] = -2,
        ret["err_msg"] = "Password is too long"
    else:
        user,flag = Users.objects.get_or_create(name=username,password=password)    # 注册，由于作者偷懒，并未对密码加密
        if flag == False:
            ret["err_code"] = -3,
            ret["err_msg"] = "The username has been used"
    return HttpResponse(json.dumps(ret),content_type="application/json")

def login_view(request):
    '''
    登陆
    '''
    username = request.POST['username']
    password = request.POST['password']
    login_time = int(request.POST.get("login_time","24")) # 登陆时长
    ret = json_reg.copy()
    try:
        user = Users.objects.get(name=username,password=password)
    except Exception as e:
        user = None
    if user:
        request.session['login'] = username
        request.session.set_expiry(3600 * login_time)   #设置登陆时长

        if request.META.get('HTTP_X_FORWARDED_FOR',None):
            ip =  request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        
        user.login_time = login_time # 更改登陆时长
        user.update_ip = ip         # 获取ip
        user.update_date = datetime.datetime.now()  # 获取时间
        user.save()
    else:
        ret["err_code"] = -1
        ret["err_msg"] = "Login failed"
    return HttpResponse(json.dumps(ret),content_type="application/json")

def profile_view(request):
    '''
    用户页面
    '''
    ret = json_reg.copy()
    username = request.session.get("login","")
    if username != "":
        ret['username'] = username
    else:
        ret['err_code'] = -1
        ret["err_msg"] = "User is not login yet."
    return HttpResponse(json.dumps(ret),content_type="application/json")

def logout_view(request):
    '''
    登出
    '''
    ret = json_reg.copy()
    username = request.session.get("login","")
    if username != "":

        try:
            user = Users.objects.get(name=username)
        except Exception:
            ret['err_code'] = -2
            ret["err_msg"] = "Username illegal."
        
        request.session["login"] = ""
        request.set_expiry = -1
        if request.META.get('HTTP_X_FORWARDED_FOR',None):
            ip =  request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        
        user.update_ip = ip         # 获取ip
        user.update_date = datetime.datetime.now()  # 获取时间
        user.save()

    else:
        ret['err_code'] = -1
        ret["err_msg"] = "User is not login yet."
    return HttpResponse(json.dumps(ret),content_type="application/json")


def chart_view(request):
    '''
    生成图标
    '''
    ret = json_reg.copy()
    y_str = request.POST.get("number","[]")
    try:
        y_axis = json.loads(y_str)
    except :
        ret['err_code'] = -2
        ret["err_msg"] = "JSON decode failed."
        return HttpResponse(json.dumps(ret),content_type="application/json")
    x_axis = range(len(y_axis))

    if len(y_axis) == 0:
        ret['err_code'] = -1
        ret["err_msg"] = "Cann't find data."
        return HttpResponse(json.dumps(ret),content_type="application/json")

    else:
        filename = str(hash(repr(y_str))) + ".png"  # hash 如果重名则不重复画图
        file = os.path.join("./images/",filename)
        if not os.path.exists(file):
            plt.plot(x_axis, y_axis)
            plt.savefig(file)
            plt.close()
        
        file_body = open(file,'rb')  
        response =StreamingHttpResponse(file_body)  
        response['Content-Type']='image/png'  
        response['Content-Disposition']='attachment;filename="'+filename+'"'  
        return response   

        
    




