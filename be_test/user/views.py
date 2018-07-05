from django.http.response import JsonResponse
from be_test import errors


def register(request):
    return JsonResponse(errors.NOT_IMPLEMENTED)


def login(request):
    return JsonResponse(errors.NOT_IMPLEMENTED)


def logout(request):
    return JsonResponse(errors.NOT_IMPLEMENTED)
