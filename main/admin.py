import json
from django.contrib import admin
from main.models import Contact, Newsletter, Addresses, About, Chef
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name', 'email', 'created_date')
    list_filter = ('email',)
    search_fields = ('name', 'message')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')


@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Chef)
class ChefAdmin(SummernoteModelAdmin):
    list_display = ('name', 'title')
    list_filter = ('title',)
    search_fields = ('name', 'title')
    summernote_fields = ('content',)


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'type')
    summernote_fields = ('content',)
