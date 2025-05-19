from django.shortcuts import render
from .models import Menu

def menu_view(request, menu_url=None, rest_of_url=None):
    return render(request, 'menus/home.html',
                  {'menus': Menu.objects.all()})