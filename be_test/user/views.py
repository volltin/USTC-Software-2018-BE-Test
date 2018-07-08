from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.utils import timezone

from .models import User


# Create your views here.


def index(request):
    return render (request, 'user/index.html')


def register(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
        except KeyError:
            resp = {'err_code': 1, 'err_msg': 'Username or password should not be empty.'}
        else:
            try:
                User.objects.get (username=username)
            except User.DoesNotExist:
                if len(username)==0 or len(password)==0:
                    resp = {'err_code': 1, 'err_msg': 'Username or password should not be empty.'}
                else:
                    new_user = User (username=username, password=password, last_log_in_time=timezone.now (),
                                     last_log_out_time=timezone.now (), last_log_in_IP=request.META['REMOTE_ADDR'],
                                     last_log_out_IP=request.META['REMOTE_ADDR'])
                    new_user.save ()
                    resp = {'err_code': 0, 'err_msg': ''}
            else:
                resp = {'err_code': 2, 'err_msg': 'This username is already registered.'}
        return JsonResponse(resp)


def login(request):
    if request.method == "POST":
        try:
            u = User.objects.get (username=request.POST['username'])
        except User.DoesNotExist:
            return JsonResponse ({'err_code': 3, 'err_msg': 'Username does not exist.'})
        else:
            if u.password == request.POST['password']:
                request.session['username'] = u.username
                u.last_log_in_time = timezone.now ()
                u.last_log_in_IP = request.META['REMOTE_ADDR']
                u.save ()
                return JsonResponse ({'err_code': 0, 'err_msg': ''})
            else:
                return JsonResponse ({'err_code': 4, 'err_msg': 'Wrong password.'})


def profile(request):
    username = request.session.get ("username", False)
    if username:
        return JsonResponse ({'err_code': 0, 'err_msg': '', 'username': username})
    else:
        return JsonResponse ({'err_code': 5, 'err_msg': "You are not logged in."})


def logout(request):
    username = request.session.get("username", False)
    if username:
        try:
            user = User.objects.get (username=username)
        except User.DoesNotExist:
            return JsonResponse({'err_code': 6, 'err_msg': 'User does not exist.'})
        else:
            user.last_log_out_time = timezone.now ()
            user.last_log_out_IP = request.META['REMOTE_ADDR']
            user.save ()
            del request.session['username']
            return JsonResponse({'err_code': 0, 'err_msg': ''})
    else:
        return JsonResponse({'err_code': 0, 'err_msg': ''})
