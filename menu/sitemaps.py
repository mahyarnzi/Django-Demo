from django.contrib import sitemaps
from django.urls import reverse


class MenuSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['menu:menu']

    def location(self, item):
        return reverse(item)
