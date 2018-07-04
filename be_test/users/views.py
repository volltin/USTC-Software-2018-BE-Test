import json

from django.shortcuts import render
from django.http import HttpResponse
from users.models import Users

# Create your views here.

json_reg = {
    "err_code":0,
    "err_msg":"",
}

def regis(request):
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
        ret["err_msg"] = "Password is too long."
    else:
        user,flag = Users.objects.get_or_create(name=username,password=password)
        if flag == False:
            ret["err_code"] = -3,
            ret["err_msg"] = "Username has been existed."
    return HttpResponse(json.dumps(ret),content_type="application/json")



