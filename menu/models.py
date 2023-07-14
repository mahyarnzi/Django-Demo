from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill  # or try ResizeToFill
from django.urls import reverse


class Meal(models.Model):
    ORDER_CHOICES = [(i, i) for i in range(1, 7)]
    order = models.IntegerField(choices=ORDER_CHOICES, default=1)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Menu(models.Model):
    image = ProcessedImageField(upload_to='menu/', format='JPEG', processors=[ResizeToFill(1366, 768)],
                                options={'quality': 80}, default='default/no-image.jpg')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(160, 120)],
                                     format='JPEG',
                                     options={'quality': 70})
    name = models.CharField(max_length=50)
    meal = models.ForeignKey(Meal, on_delete=models.RESTRICT)
    content = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=False)
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['meal__order', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu:menu')

