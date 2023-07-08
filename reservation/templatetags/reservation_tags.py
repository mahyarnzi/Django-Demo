from django import template

register = template.Library()


@register.filter()
def image_url(queryset, title):
    result = queryset.filter(title=title).first()
    return result.image.url
