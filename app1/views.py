from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def samplex(request):
    return HttpResponse('<h1>This is samplex function of app1</h1>')

def sampley(request):
    return HttpResponse('<h1>This is sampley function of app2</h1>')