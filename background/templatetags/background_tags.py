from django import template
from background.models import Logo, Background

register = template.Library()


@register.simple_tag(name='logo')
def function():
    logo = Logo.objects.filter(title='logo').first()
    return logo


@register.simple_tag(name='background')
def function():
    background = Background.objects.all()
    return background


@register.filter()
def image_thumbnail_url(queryset, title):
    result = queryset.filter(title=title).first()
    return result.image_thumbnail.url


@register.filter()
def image_url(queryset, title):
    result = queryset.filter(title=title).first()
    return result.image.url
