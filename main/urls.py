from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main.views import *


app_name = 'website'
urlpatterns = [
    path('', index_view, name='index'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('newsletter/', newsletter_view, name='newsletter'),
    path('maintenance/', maintenance_view, name='maintenance'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)