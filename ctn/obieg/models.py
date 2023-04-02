from django.db import models
from datetime import datetime

def user_directory_path(instance, filename):
    filename = datetime.now().strftime('%Y%m%d%H%M%S%f') + ".pdf"
    rok = filename[:4]
    miesiac = filename[4:6]
    path = rok + '/' + miesiac
    return 'pdf/{0}/{1}'.format(path, filename)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)