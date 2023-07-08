from django.utils import timezone
from django import template
from blog.models import Post, Category, Comment

register = template.Library()


@register.simple_tag(name='latest_posts')
def function(arg=3):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return posts


@register.inclusion_tag('blog/blog_popular.html')
def popular_posts_blogpage(arg=3):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-counted_views')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog_category.html')
def categories_count():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    categories = Category.objects.all()
    category_dict = {}
    for name in categories:
        category_dict[name] = posts.filter(category=name).count()
    return {'categories': category_dict}


@register.inclusion_tag('blog/blog_archive.html')
def archives_blog():
    archives = {}
    arch = Post.objects.dates('published_date', 'month', order='DESC')

    for item in arch:
        key = item.strftime('%B %Y')
        value = Post.objects.filter(published_date__month=item.month, published_date__year=item.year).count()
        archives[key] = value
    return {'archives': archives}


@register.simple_tag(name='comments_count')
def function(post):
    comments_count = Comment.objects.filter(post=post).count()
    return comments_count


@register.filter()
def image_url(queryset, title):
    result = queryset.filter(title=title).first()
    return result.image.url
