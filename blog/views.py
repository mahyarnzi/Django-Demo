from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.contrib import messages
from calendar import month_name


# Create your views here.
def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-published_date')
    if 'cat_name' in kwargs:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if 'author_username' in kwargs:
        posts = posts.filter(author__username=kwargs['author_username'])
    if 'month' in kwargs:
        calender = {month: index for index, month in enumerate(month_name) if month}
        posts = posts.filter(published_date__month=calender[kwargs['month']], published_date__year=kwargs['year'])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 '{} ,your comment has been submitted successfully.'.format(request.POST['name']))
        else:
            messages.add_message(request, messages.ERROR, 'Your comment has not been submitted. Please try again.')
    post = get_object_or_404(Post, id=pid, status=1, published_date__lte=timezone.now())
    comments = Comment.objects.filter(post=post, approved=True)
    next_post = Post.objects.filter(published_date__gt=post.published_date, published_date__lte=timezone.now(),
                                    status=1).order_by('published_date').first()
    previous_post = Post.objects.filter(published_date__lt=post.published_date, published_date__lte=timezone.now(),
                                        status=1).order_by('published_date').last()
    post.increase_counted_views()
    form = CommentForm()
    context = {'post': post, 'next_post': next_post, 'previous_post': previous_post, 'comments': comments, 'form': form}
    return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-published_date')
    if request.method == 'GET':
        if q := request.GET.get('q'):
            posts = posts.filter(content__contains=q)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)
