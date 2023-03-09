from django.urls import path
from app2.views import *
app_name='nothing'
urlpatterns=[
    path('samplea/',samplea,name='samplea'),
    path('sampleb/',sampleb,name='sampleb'),
]