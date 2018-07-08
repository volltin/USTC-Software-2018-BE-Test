import json
import datetime
import os
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import forms
from . import models
# Create your views here.

json_reg = {
    "err_code":0,
    "err_msg":"",
}

#def index(request):
    #pass

def login(request):
    ret = json_reg.copy()
    if request.session.get('is_login', None):
        ret["err_code"] = -3
        ret["err_msg"] = "Please logout before login"
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        # message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
                    #return redirect('/index/')
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    ret["err_code"] = 0
                    ret["err_msg"] = ""
                else:
                    ret["err_code"] = -1
                    ret["err_msg"] = "Password does not correst"
            except:
                ret["err_code"] = -2
                ret["err_msg"] = "Username does not exist"
        return HttpResponse(json.dumps(ret), content_type="application/json")
    login_form = forms.UserForm()
    return HttpResponse(json.dumps(ret), content_type="application/json")

def logout(request):
    ret = json_reg.copy()
    if not request.session.get('is_login', None):
        ret["err_code"] = -1
        ret["err_msg"] = "Please login before you logout"
        return HttpResponse(json.dumps(ret), content_type="application/json")
    request.session.flush()
    ret["err_code"] = 0
    ret["err_msg"] = ""
    return HttpResponse(json.dumps(ret), content_type="application/json")

def register(request):
    ret = json_reg.copy()
    if request.session.get('is_login', None):
        ret["err_code"] = -1
        ret["err_msg"] = "Please logout before you register"
        return HttpResponse(json.dumps(ret), content_type="application/json")
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            if password1 != password2:
                ret["err_code"] = -2
                ret["err_msg"] = "Passwords are different"
                return HttpResponse(json.dumps(ret), content_type="application/json")
            else:
                same_name_user = models.User.objects.filter(username=username)
                if same_name_user:
                    ret["err_code"] = -3
                    ret["err_msg"] = "Username has been used"
                    return HttpResponse(json.dumps(ret), content_type="application/json")
                #用户名合法且密码输入正确
                new_user = models.User()
                new_user.username = username
                new_user.password = password1
                new_user.save()
                ret["err_code"] = 0
                ret["err_msg"] = ""
                return HttpResponse(json.dumps(ret), content_type="application/json")
    register_form = forms.RegisterForm()
    return HttpResponse(json.dumps(ret), content_type="application/json")

def profile(request):
    ret = json_reg.copy()
    if request.session.get('is_login', None):
        ret["username"] = request.session.get('is_login', None)
    else:
        ret["err_code"] = -1
        ret["err_msg"] = "Please login to get your profile"
    return HttpResponse(json.dumps(ret), content_type="application/json")