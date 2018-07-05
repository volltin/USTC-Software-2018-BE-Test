from django.contrib import auth
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from ipware import get_client_ip
from user import errors
from user.models import User, Profile, USERNAME_MAX, PASSWORD_MAX
from user import utils


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.user.is_authenticated:
        return JsonResponse(errors.LOGGED_IN)

    username = (request.GET or request.POST).get('username')
    password = (request.GET or request.POST).get('password')

    if not username or not password:
        return JsonResponse(errors.INSUFFICIENT_ARGS)

    if len(username) > USERNAME_MAX:
        return JsonResponse(errors.USERNAME_TOO_LONG)
    if len(password) > PASSWORD_MAX:
        return JsonResponse(errors.PASSWORD_TOO_LONG)
    if not utils.is_well_formed_username(username):
        return JsonResponse(errors.ILLEGAL_USERNAME)
    if not utils.is_well_formed_password(password):
        return JsonResponse(errors.ILLEGAL_PASSWORD)
    if not utils.is_secure_password(password):
        return JsonResponse(errors.PASSWORD_TOO_SIMPLE)

    if User.objects.filter(username=username).exists():
        return JsonResponse(errors.USER_EXISTS)

    user = User.objects.create_user(username=username, password=password)
    profile = Profile.objects.create(user_id=user.id, last_ip=get_client_ip(request)[0])
    user.save()
    profile.save()
    return JsonResponse(errors.SUCCESS)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return JsonResponse(errors.LOGGED_IN)

    username = (request.GET or request.POST).get('username')
    password = (request.GET or request.POST).get('password')

    if not username or not password:
        return JsonResponse(errors.INSUFFICIENT_ARGS)

    user = User.objects.filter(username=username).exists()
    if not user:
        return JsonResponse(errors.USER_NOT_EXISTS)

    user = auth.authenticate(username=username, password=password)
    if user:
        profile = Profile.objects.get(user_id=user.id)
        profile.last_ip = get_client_ip(request)[0]
        auth.login(request, user)
        return JsonResponse(errors.SUCCESS)
    else:
        return JsonResponse(errors.INVALID_CREDS)


@require_http_methods(['GET', 'POST'])
def logout(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=request.user.id)
        profile.last_ip = get_client_ip(request)[0]
        auth.logout(request)
        return JsonResponse(errors.SUCCESS)
    else:
        return JsonResponse(errors.NOT_LOGGED_IN)


@require_http_methods(['GET', 'POST'])
def profile(request):
    if request.user.is_authenticated:
        return JsonResponse({'username': request.user.username, **errors.SUCCESS})
    else:
        return JsonResponse({'username': '', **errors.NOT_LOGGED_IN})
