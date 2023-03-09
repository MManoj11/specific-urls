from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def samplea(request):
    return HttpResponse('<h1>This is samplea function of app2</h1>')

def sampleb(request):
    return HttpResponse('<h1>This is sampleb function of app2</h1>')