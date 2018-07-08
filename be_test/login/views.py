from django.shortcuts import render, redirect
import json
from django.http import HttpResponse
from .forms import UserRegisterForm, UserLoginForm
from django.urls import reverse
from django.contrib import auth
from .models import UserMain
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

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


# ------------
# 注册操作实现
# 传入没有使用过的用户名时能够注册成功，并返回 err_code 为 0
# 采用自定义的检验器, 首字母必须是字母或者下划线, 长度6-20
# 采用默认密码验证器
# code: {0: '', 1: 'username is not valid', 2: 'username has been registered', 3: 'password is not valid' }
# author: roar
# ------------
def register(request):
    if request.method == 'GET':
        username = request.GET.get('username', '')
        password = request.GET.get('password', '')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

    if UserMain.objects.filter(username=username):
        resp = {'err_code': 2, 'err_msg': 'username has been registered'}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    try:
        password_validation.validate_password(password, username)
    except ValidationError:
        resp = {'err_code': 3, 'err_msg': 'password is not valid'}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    try:
        new_account = UserMain()
        new_account.username = username
        new_account.password = make_password(password)
        new_account.email = 'abc@def.com'
        new_account.save()
    except ValidationError:
        resp = {'err_code': 1, 'err_msg': 'username is not valid'}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    resp = {'err_code': 0, 'err_msg': ''}
    return HttpResponse(json.dumps(resp), content_type="application/json")


# ------------
# 个人信息
# 如果用户已经登陆，在 username 中返回登陆的用户名，否则为空；
# 如果用户未登陆，返回错误信息；
# code: {0: '', 1: 'you have not been login yet'}
# author: roar
# ------------
def profile(request):
    if request.user.is_authenticated:
        user = request.user
        resp = {'err_code': 0, 'err_msg': '', 'username': user.username}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    else:
        resp = {'err_code': 1, 'err_msg': 'you have not been login yet'}
        return HttpResponse(json.dumps(resp), content_type="application/json")


# ------------
# 登出
# 清除登陆的凭证（session）；
# code: {0: ''}
# author: roar
# ------------
def logout(request):
    auth.logout(request)
    resp = {'err_code': 0, 'err_msg': ''}
    return HttpResponse(json.dumps(resp), content_type="application/json")