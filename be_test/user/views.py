from django.shortcuts import render
from . import models
from .forms import UserForm
import json
from django.http import JsonResponse

# Create your views here.

#可能出现的返回值
resp_true = {
    "err_code":0,
    "err_msg":""
}
resp_err1 = {
    "err_code":1,
    "err_msg":"User Exists"
}
resp_err2 = {
    "err_code":2,
    "err_msg":"User Has Not Logged in"
}
resp_err3 = {
    "err_code":3,
    "err_msg":"Wrong Password"
}
resp_err4 = {
    "err_code":4,
    "err_msg":"User Does Not Exist"
}
resp_err5 = {
    "err_code":5,
    "err_msg":"User Has Logged in"
}

def register(request):
    if request.method == "POST":
        register_form = UserForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            same_name_user = models.User.objects.filter(name = username)
            if same_name_user:#用户名已存在，不可用该用户名注册
                return JsonResponse(resp_err1)
            new_user = models.User.objects.create()
            new_user.name = username
            new_user.password = password
            new_user.save()#注册成功
            return JsonResponse(resp_true)
    register_form = UserForm()
    return JsonResponse(resp_true)

def login(request):
    if request.session.get('is_login', None):
        return JsonResponse(resp_err5)#用户已登录，不可二次登录
    if request.method == 'POST':
        login_form = UserForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name = username)
                if user.password == password:
                    request.session['is_login'] = True #设置session
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return JsonResponse(resp_true)#登录成功
                else:
                    return JsonResponse(resp_err3)#密码错误
            except:
                return JsonResponse(resp_err4)#用户名不存在
        return JsonResponse(resp_true)
    login_form = UserForm()
    return JsonResponse(resp_true)

def profile(request):
    if not request.session.get('is_login', None):
        return JsonResponse(resp_err2)#用户未登录，则不可显示个人信息
    username = request.session['user_name']
    return JsonResponse({"err_code":0,"err_msg":"","username":username})

def logout(request):
    if not request.session.get('is_login', None):
        return JsonResponse(resp_err2)#用户未登录，则不可登出
    del request.session['is_login']#清除session
    del request.session['user_id']
    del request.session['user_name']
    return JsonResponse(resp_true)

