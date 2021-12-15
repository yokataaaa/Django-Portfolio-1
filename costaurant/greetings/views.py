from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloindex(request):
    return HttpResponse('<h2> Hola! :) </h2>')