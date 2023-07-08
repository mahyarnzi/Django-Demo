from django.contrib import admin
from .models import CustomUser, Background


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'date_joined']

@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ['title']
