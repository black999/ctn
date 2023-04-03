from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index , name='index'),
    path('upload/', views.upload, name='upload'),
    path('docs_view', views.docs_view, name='docs_view'),
    path('doc/<int:pk>', views.doc_details, name='doc_details'),
    path('doc/<int:pk>/del', views.doc_del, name='doc_del'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)