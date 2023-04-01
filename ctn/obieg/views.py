from django.shortcuts import render
from django.conf import settings
from datetime import datetime
from django.contrib.auth.decorators import login_required
import os

@login_required
def index(request):
    return render(request, 'obieg/index.html')


def upload(request):
    fname = datetime.now().strftime('%Y%m%d%H%M%S%f')
    rok = fname[:4]
    miesiac = fname[4:6]
    path = os.path.join(settings.MEDIA_ROOT, 'pdf', rok, miesiac)
    if not os.path.exists(path):
        os.makedirs(path)
    return render(request, 'obieg/index.html')