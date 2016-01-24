from django.shortcuts import render 
from django.http import HttpResponse

def oldindex(request):
    return HttpResponse("Rango Sasy hey there world <br/> <a href='/rango/about'>About </a>")

def oldabout(request):
    return HttpResponse("Rango Say: Hellworld <br/> <a href='/rango/'> Home Page </a> ")

def oldcontact(request):
    return HttpResponse("<a href='/rango/'> About </a> " )

def index (request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render (request, 'rango/index.html', context_dict )

def about (request):
    context_dict = {'boldmessage': " I am bold font about page hi"}
    return render (request, 'rango/index.html', context_dict)

def contact(request):
    context_dict = {'boldmessage': " I am contact page hi "}
    return render (request, 'rango/index.html', context_dict)
