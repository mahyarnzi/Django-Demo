from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill  # or try ResizeToFill


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = ProcessedImageField(upload_to='blog/', format='JPEG', processors=[ResizeToFill(1366, 768)],
                                options={'quality': 80}, default='default/no-image.jpg')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(160, 120)],
                                     format='JPEG',
                                     options={'quality': 70})
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category, )
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def increase_counted_views(self):
        self.counted_views += 1
        self.save()

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid': self.id})


class Comment(models.Model):
    name = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField()
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.name


class Background(models.Model):
    image = ProcessedImageField(upload_to='background/', format='JPEG', processors=[ResizeToFill(1440, 900)],
                                options={'quality': 80}, default='default/no-image.jpg')
    title_list = ['blog_home', 'blog_single']
    TITLE_CHOICE = [(i, i) for i in title_list]
    title = models.CharField(choices=TITLE_CHOICE, unique=True, null=True, blank=True, max_length=20)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
