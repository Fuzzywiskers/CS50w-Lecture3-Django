from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def malia(request):
    return HttpResponse("Hello Malia")

def greet(request, name):
    return render(request, "hello/greet.html", {        #providing information witht the key of name and passing on a value onto the html page#
        "name": name.capitalize()
    })