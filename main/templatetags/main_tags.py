from django import template
from main.models import About

register = template.Library()


@register.simple_tag(name='about')
def function():
    about = About.objects.all()
    features = about.filter(type='Feature').order_by('-updated_date')[:3]
    summary = about.filter(type='Summary').order_by('-updated_date').first()
    return {'features': features, 'summary': summary}


@register.filter()
def split(value, arg):
    return str(value).split(' ')[int(arg) - 1]

