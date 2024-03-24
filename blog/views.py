from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    #return HttpResponse("Home!")
    return render(request, 'home.html')
    

def About(request):
    #return HttpResponse("About!")
    return render(request, 'about.html')