from django.shortcuts import render
from .models import Menu


def menu_view(request):
    menus = Menu.objects.filter(status=1)
    starter = menus.filter(meal__name='Starter').order_by('name')
    breakfast = menus.filter(meal__name='BreakFast').order_by('name')
    lunch = menus.filter(meal__name='Lunch').order_by('name')
    dinner = menus.filter(meal__name='Dinner').order_by('name')
    dessert = menus.filter(meal__name='Dessert').order_by('name')
    drink = menus.filter(meal__name='Drink').order_by('name')

    context = {'starter': starter, 'breakfast': breakfast, 'lunch': lunch, 'dinner': dinner,
               'dessert': dessert,
               'drink': drink}
    return render(request, 'menu/menu.html', context)
