from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from datetime import datetime
from django.contrib.auth.decorators import login_required
import os
from django.core.files.storage import FileSystemStorage
from obieg.forms import DocumentForm
from obieg.models import *

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
            pk = str(Document.objects.last().id)
            print(pk)
            return redirect('/doc/' + pk)
    else:
        form = DocumentForm()
    return render(request, 'obieg/upload.html', {
        'form': form,
        'title': 'Przesyłanie dokumentu',
    })

def docs_view(request):
    dokumenty = Document.objects.all()
    context = {
        'docs' : dokumenty,
        'title' : 'Przeslane dokumenty',
    }
    return render(request, 'obieg/docs.html', context)

def doc_details(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    context = {
        'doc' : doc,
        'title' : 'Przesłany dokument',
    }
    return render(request, 'obieg/doc_details.html', context)

@login_required
def doc_del(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    doc.delete()
    return redirect('docs_view')