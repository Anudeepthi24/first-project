from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Ram(request):
    return HttpResponse("Hi How are you")

def krish(request):
    return HttpResponse('hello')
