from django.contrib import admin
from .models import Background, Logo


@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ['title']
