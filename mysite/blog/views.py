from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django!")

def about(request):
    return render(request, "blog/about.html")

def home(request):
    context = {
        "title": "My first blog",
        "message": "I am glad to see you, my friend!",
    }
    return render(request, "blog/home.html", context)