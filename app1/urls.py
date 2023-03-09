from app1.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('samplex/',samplex,name='samplex'),
    path('sampley/',sampley,name='sampley'),
]