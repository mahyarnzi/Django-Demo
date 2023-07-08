from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from menu.sitemaps import MenuSitemap
from reservation.sitemaps import ReservationSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
    'menu': MenuSitemap,
    'reservation': ReservationSitemap
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', include('robots.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('accounts.urls')),
    path('menu/', include('menu.urls')),
    path('reservation/', include('reservation.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
