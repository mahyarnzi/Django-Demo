from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill  # or try ResizeToFill


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, error_messages={'unique': (
        "A user with that email already exists.")})

    phone = PhoneNumberField(null=True, blank=True, unique=True, error_messages={'unique': (
        "A user with that phone number already exists.")})


class Background(models.Model):
    image = ProcessedImageField(upload_to='background/', format='JPEG', processors=[ResizeToFill(1440, 900)],
                                options={'quality': 80}, default='default/no-image.jpg')

    title = models.CharField(choices=(('account', 'account'),), unique=True, null=True, blank=True, max_length=20)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
