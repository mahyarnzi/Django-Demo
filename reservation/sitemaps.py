from django.contrib import sitemaps
from django.urls import reverse


class ReservationSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['reservation:reservation']

    def location(self, item):
        return reverse(item)
