from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from menu.views import *
from menu.feeds import MenuFeed

app_name = 'menu'
urlpatterns = [
    path('', menu_view, name='menu'),
    path('rss/feed/', MenuFeed()),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
