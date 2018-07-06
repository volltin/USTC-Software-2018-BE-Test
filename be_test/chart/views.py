from django.http.response import FileResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from chart import errors
from io import BytesIO
from expiringdict import ExpiringDict

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


_cache = ExpiringDict(max_len=100, max_age_seconds=60)


@require_POST
@csrf_exempt
def simple(request):
    raw_data = request.POST.get('data')
    width = request.POST.get('width', 8)
    height = request.POST.get('height', 6)
    dpi = request.POST.get('dpi', 96)

    # Sanity checks
    if not raw_data:
        return JsonResponse(errors.INSUFFICIENT_ARGS)

    try:
        ys = raw_data.split()
        ys = list(map(float, ys))
        if len(ys) == 0:
            raise ValueError
    except ValueError:
        return JsonResponse(errors.INVALID_DATA)

    if width <= 0 or height <= 0:
        return JsonResponse(errors.INVALID_SIZE)

    # Check if already cached
    key = (raw_data, width, height, dpi)
    if key in _cache:
        buffer = BytesIO()
        buffer.write(_cache[key])
        buffer.seek(0)
        return FileResponse(buffer, content_type='image/png')
    else:
        # If not, generate image data
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        ax = fig.add_subplot(111)
        ax.plot(ys)
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        # Put it in the cache
        content = buffer.read()
        _cache[key] = content
        buffer.seek(0)
        return FileResponse(buffer, content_type='image/png')
