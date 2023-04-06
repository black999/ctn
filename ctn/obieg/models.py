from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator

def user_directory_path(instance, filename):
    filename = datetime.now().strftime('%Y%m%d%H%M%S%f') + ".pdf"
    rok = filename[:4]
    miesiac = filename[4:6]
    path = rok + '/' + miesiac
    return 'pdf/{0}/{1}'.format(path, filename)

zuzyto_cel_wybor = [
        ('opcja1', 'opcja1'),
        ('opcja2', 'opcja2'),
        ('opcja3', 'opcja3'),
    ]

rodzaj_dokumentu_wybor = [
    ('skan', 'skan'),
    ('elektroniczny', 'elektroniczny'),
]

#def last_of_cel():
#    return Zuzycie_cel.objects.last().id

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path, validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    data_dok = models.DateField(null=True, blank=True)
    zuzyto_cel = models.CharField(max_length=30, choices=zuzyto_cel_wybor)
    rodzaj_dokumentu = models.CharField(max_length=20, choices=rodzaj_dokumentu_wybor)
    ksieg_wn1 = models.CharField(max_length=10, blank=True)
    ksieg_wn2 = models.CharField(max_length=10, blank=True)
    ksieg_wn3 = models.CharField(max_length=10, blank=True)
    ksieg_wn4 = models.CharField(max_length=10, blank=True)
    ksieg_ma1 = models.CharField(max_length=10, blank=True)
    ksieg_ma2 = models.CharField(max_length=10, blank=True)
    ksieg_ma3 = models.CharField(max_length=10, blank=True)
    ksieg_ma4 = models.CharField(max_length=10, blank=True)
