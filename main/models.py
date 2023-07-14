from django.db import models
from accounts.models import CustomUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill  # or try ResizeToFill
from osm_field.fields import LatitudeField, LongitudeField, OSMField


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.email


class Addresses(models.Model):
    title = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    work_start_time = models.TimeField()
    work_end_time = models.TimeField()
    iframe_url = models.URLField(null=True, blank=True, max_length=500)
    latitude = LatitudeField(null=True, blank=True)
    longitude = LongitudeField(null=True, blank=True)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.title


class About(models.Model):
    image = ProcessedImageField(upload_to='about/', format='JPEG', processors=[ResizeToFill(393, 393)],
                                options={'quality': 80}, default='default/no-image.jpg')
    TYPE_CHOICES = [('Summary', 'Summary'), ('Feature', 'Feature')]
    type = models.CharField(choices=TYPE_CHOICES, default='Feature', max_length=10)
    title = models.CharField(max_length=40, null=True, blank=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['type', '-title']

    def __str__(self):
        return self.title


class Chef(models.Model):
    image = ProcessedImageField(upload_to='about/', format='JPEG', processors=[ResizeToFill(320, 320)],
                                options={'quality': 80}, default='default/no-avatar.jpg')

    name = models.CharField(max_length=25)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

