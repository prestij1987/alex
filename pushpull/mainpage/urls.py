

from django.urls import path
from . import views

urlpatterns = [
    path('',        views.index,  name='home'),
    path('uslugi/', views.uslugi, name='home'),
    #path('mystring/', func_start, name='mystring')
    
]
