from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django!")

def about(request):
    return render(request, "blog/about.html")

def home(request):
    context = {
        "title": "my first blog",
        "message": "I am glad to see you, my friend!",
        "is_published": False,
        "posts": [
            "My first post",
            "I am studying Django",
            "My project plan"
        ],
        "test": [],
        "new_posts": [
            {
            "title": "Django basic",
            "author": "Shawn",
            "published": True
        },
        {
            "title": "Django advanced level",
            "author": "Rachel",
            "published": False
        }
        ]
    }
    return render(request, "blog/home.html", context)