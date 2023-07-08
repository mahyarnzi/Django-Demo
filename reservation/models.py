from django.db import models
from accounts.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill  # or try ResizeToFill


class Table(models.Model):
    name = models.CharField(max_length=255)
    min_seats = models.IntegerField()
    max_seats = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.RESTRICT)
    count = models.IntegerField()
    name = models.CharField(max_length=255)
    phone = PhoneNumberField(null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    time = models.TimeField()
    date = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class ReservationContact(models.Model):
    type = models.CharField(max_length=25)
    content = models.TextField()

    def __str__(self):
        return self.type


class Background(models.Model):
    image = ProcessedImageField(upload_to='background/', format='JPEG', processors=[ResizeToFill(1440, 900)],
                                options={'quality': 80}, default='default/no-image.jpg')
    title_list = ['reservation']
    TITLE_CHOICE = [(i, i) for i in title_list]
    title = models.CharField(choices=TITLE_CHOICE, unique=True, null=True, blank=True, max_length=20)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
