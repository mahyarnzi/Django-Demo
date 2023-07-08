from django import template
from accounts.models import Background
register = template.Library()


@register.simple_tag(name='background')
def function():
    background = Background.objects.first()
    return background.image.url