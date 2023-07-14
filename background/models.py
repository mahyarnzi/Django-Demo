from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill  # or try ResizeToFill


class Background(models.Model):
    image = ProcessedImageField(upload_to='background/', format='webp', processors=[ResizeToFill(1440, 900)],
                                options={'quality': 80}, default='default/no-image.jpg')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(400, 300)],
                                     format='webp',
                                     options={'quality': 80})

    title_list = ['home_top', 'home_bottom', 'home_middle_1', 'home_middle_2', 'about_top', 'about_bottom',
                  'about_middle', 'contact', 'account', 'maintenance', 'blog_home', 'blog_single', 'reservation',
                  'menu_starter', 'menu_breakfast', 'menu_lunch', 'menu_dinner', 'menu_dessert', 'menu_drink']
    TITLE_CHOICE = [(i, i) for i in title_list]
    title = models.CharField(choices=TITLE_CHOICE, unique=True, null=True, blank=True, max_length=20)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Logo(models.Model):
    logo_background = ProcessedImageField(upload_to='logo/', format='png', processors=[ResizeToFill(100, 100)],
                                          options={'quality': 100})
    logo_no_background = ProcessedImageField(upload_to='logo/', format='png', processors=[ResizeToFill(100, 100)],
                                             options={'quality': 100})
    icon = ProcessedImageField(upload_to='logo/', format='png', processors=[ResizeToFill(35, 35)],
                               options={'quality': 100})

    title = models.CharField(choices=(('logo', 'logo'),), unique=True, null=True, blank=True, max_length=20)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
