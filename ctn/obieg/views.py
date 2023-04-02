from django.shortcuts import render, redirect
from django.conf import settings
from datetime import datetime
from django.contrib.auth.decorators import login_required
import os
from django.core.files.storage import FileSystemStorage
from obieg.forms import DocumentForm
from django.http import FileResponse

@login_required
def index(request):
    return render(request, 'obieg/index.html')


def upload_old(request):
    if request.method == 'POST' and request.FILES['myfile']:
        fname = datetime.now().strftime('%Y%m%d%H%M%S%f') + ".pdf"
        rok = fname[:4]
        miesiac = fname[4:6]
        path = os.path.join(settings.MEDIA_ROOT, 'pdf', rok, miesiac)
        if not os.path.exists(path):
            os.makedirs(path)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.location = path
        print(fs.location)
        fs.path(path)
        filename = fs.save(fname, myfile)
    return render(request, 'obieg/index.html')

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_view')
    else:
        form = DocumentForm()
    return render(request, 'obieg/upload.html', {
        'form': form
    })

def pdf_view_old(request):
    with open(settings.MEDIA_ROOT + '/pdf/2023/04/20230402174236732512.pdf', 'rb') as pdf:
         response = FileResponse(pdf.read(), content_type='application/pdf')
         response['Content-Disposition'] = 'filename=a.pdf'
         return response
    pdf.closed

def pdf_view(request):
    return render(request, 'obieg/pdf_view.html')

