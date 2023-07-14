from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, error_messages={'unique': (
        "A user with that email already exists.")})

    phone = PhoneNumberField(null=True, blank=True, unique=True, error_messages={'unique': (
        "A user with that phone number already exists.")})
