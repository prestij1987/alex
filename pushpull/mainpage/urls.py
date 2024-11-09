

from django.urls import path
from . import views

urlpatterns = [
    path('',             views.index,      name='home'),
    path('uslugi/',      views.uslugi,     name='uslugi'),
    path('park/',        views.park,       name='park'),
    path('otzyvi/',      views.otzyv,      name='otzyvi'),
    path('formaotvet/',  views.formaotvet, name='formaotvet'),
    #path('mystring/', func_start, name='mystring'),
    
]
