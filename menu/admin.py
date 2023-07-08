from django.contrib import admin
from menu.models import Menu, Meal, Background


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'meal']


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ['title']
