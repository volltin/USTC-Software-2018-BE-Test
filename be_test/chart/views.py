from django.http.response import JsonResponse
from be_test import errors


def simple(request):
    return JsonResponse(errors.NOT_IMPLEMENTED)
