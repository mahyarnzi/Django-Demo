from django import template
from menu.models import Background, Menu

register = template.Library()


@register.simple_tag(name='menu')
def function():
    background = Background.objects.all()
    return background


@register.simple_tag(name='gallery')
def function(arg=8):
    gallery = Menu.objects.all().order_by('-updated_date')
    photo_list = []
    for item in gallery[:arg]:
        photo_list.append((item.image.url, item.image_thumbnail.url))
    return photo_list


@register.filter()
def image_thumbnail_url(queryset, title):
    result = queryset.filter(title=title).first()
    return result.image_thumbnail.url
