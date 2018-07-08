from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from .forms import UserRegisterForm, UserLoginForm
from from django.urls import reverse
from django.contrib import auth

# Create your views here.


# ------------
# 登入操作实现
# 用户名密码正确时，登陆成功，并设置 session 为登录状态，返回登陆成功的代码；
# 用户名密码错误时，返回错误信息；
# code: {0: '', 1: 'username or password error' }
# author: roar
# ------------
def login(request):
    # 如果当前已有用户登入, 则直接跳转到主页
    if request.user.is_authenticated:
        return redirect(reverse('profile'))

    if request.method == 'GET':
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')

    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        resp = {'err_code': 0, 'err_msg': ''}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    else:
        resp = {'err_code': 1, 'err_msg': 'username or password error'}
        return HttpResponse(json.dumps(resp), content_type="application/json")

