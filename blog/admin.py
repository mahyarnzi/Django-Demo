from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['title', 'author', 'counted_views', 'status', 'published_date', 'created_date']
    search_fields = ['title', 'content', 'author']
    list_filter = ['status']
    summernote_fields = ('content',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ['name', 'post', 'approved', 'created_date']
    list_filter = ['post', 'approved']
    summernote_fields = ('content',)
    search_fields = ['name', 'post']
