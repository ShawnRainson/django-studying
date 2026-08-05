from django.shortcuts import render

def home(request):
    context = {
        "title": "Main page",
        "username": "Shawn",
        "posts": [
            "First page",
            'Django studying',
            'My first project'
        ]
        }
    return render(request, "blog/home.html", context)