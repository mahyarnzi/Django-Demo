from django import template
from main.models import About, Logo

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


@register.filter()
def image_url(queryset, title):
    result = queryset.filter(title=title).first()
    return result.image.url


@register.simple_tag(name='logo')
def function():
    logo = Logo.objects.filter(title='logo').first()
    return logo
