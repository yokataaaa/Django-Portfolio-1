from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Menu
# Create your views here.
def index(request):
    context = dict()
    today = datetime.today().date()
    menus = Menu.objects.all()
    context['date'] = today
    context['menus'] = menus
    return render(request, 'menus/index.html', context=context)

def menu_detail(request, pk):
    context = dict()
    menu = Menu.objects.get(id=pk)
    context['menu'] = menu   
    return render(request, 'menus/detail.html', context=context )