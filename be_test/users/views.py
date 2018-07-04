import json
import datetime

from django.shortcuts import render
from django.http import HttpResponse
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
        ret["err_msg"] = "用户名太长."
    elif len(password) > 50:
        ret["err_code"] = -2,
        ret["err_msg"] = "密码太长."
    else:
        user,flag = Users.objects.get_or_create(name=username,password=password)
        if flag == False:
            ret["err_code"] = -3,
            ret["err_msg"] = "用户名已经存在."
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
        
        user.update_ip = ip         # 获取ip
        user.update_date = datetime.datetime.now()  # 获取时间
    else:
        ret["err_code"] = -1
        ret["err_msg"] = "用户名或密码错误"
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
        ret["err_msg"] = "用户未登录"
    return HttpResponse(json.dumps(ret),content_type="application/json")

def logout_view(request):
    pass




