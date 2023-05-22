from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def SaiKumar(request):
    return HttpResponse('<marquee><h1>My name is sai kumar</h1></marquee>')
def Rupesh(request):
    return HttpResponse('Sai Kumar My Name is Sai Kumar')