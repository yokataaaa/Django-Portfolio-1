from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    context = dict()
    goods = Product.objects.all()
    context['goods'] = goods
    return render(request, 'goods/index.html', context=context)
