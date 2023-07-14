from django.db import models
from accounts.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField


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
