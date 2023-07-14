from django import template
from menu.models import Menu

register = template.Library()


@register.simple_tag(name='gallery')
def function(arg=8):
    gallery = Menu.objects.all().order_by('-updated_date')
    photo_list = []
    for item in gallery[:arg]:
        photo_list.append((item.image.url, item.image_thumbnail.url))
    return photo_list
