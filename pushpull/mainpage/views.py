from django.shortcuts import render
#from django.http import HttpResponse



def index(request):
    context = {}
    return render(
        request,   # zapros
        'mainpage/index.html',  # put k shablonu
                                # podstanovka
        context
    )

def uslugi(request):
    context = {}
    return render(
        request,   # zapros
        'mainpage/html/uslugi.html',  # put k shablonu
                                # podstanovka
        context
    )


def park(request):
    context = {'park techniki' : 'Чертежи и схемы тралов'}
    return render(request,   
        'mainpage/html/park.html',  
                               
        context
    )

def otzyv(request):
    context = {}
    return render(request,   
        'mainpage/html/otzyvi.html',  
                               
        context
    )

def formaotvet(request):
    context = {}
    return render(
        request,
        'mainpage/html/formaotvet.html',
        context
    )