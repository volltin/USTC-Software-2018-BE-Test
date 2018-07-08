from django.shortcuts import render
from django.http import HttpResponse

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import io


def index(request):
    return render(request, 'chart/index.html', {'array':range(10)})


def plot(request):
    if request.method == "POST":
        dots = request.POST.getlist('array')
        x = range(len(dots))
        plt.plot(x, dots, '-')
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        response = HttpResponse(buf.getvalue(), content_type='image/png')
        plt.close()
        return response
