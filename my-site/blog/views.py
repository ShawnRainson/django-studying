from django.shortcuts import render

def home(request):
    context = {
        "name": "Shawn",
        "age": 21,
        "technologies": [
            "Python",
            'Django',
            'HTML'
        ]
        }
    return render(request, "profile/profile.html", context)