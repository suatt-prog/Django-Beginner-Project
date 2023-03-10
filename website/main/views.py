from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item
def index(response,id):
    liste=ToDoList.objects.get(id=id)
    return render(response,"main/base.html",{})
    #return HttpResponse("Coding with Suat"+str(id)+liste.name)
def v1(response):
    return HttpResponse("Page 2")
def home(response):
    return render(response,"main/home.html",{})