Вопрос 1.
Почему удобнее хранить HTML в шаблонах, а не писать всю разметку внутри HttpResponse()? - Потому-что так не будет путаницы между Python и HTML, плюс код не будет громоздким

Вопрос 2.
Что делает этот код?
return render(request, "blog/about.html") - возвращает HTTP-ответ в виде HTML-файла



Вопрос 3.
Где Django будет искать шаблон, если в представлении указано "blog/home.html"?
- A. В корне проекта рядом с manage.py.
- B. В blog/templates/blog/home.html. +
- C. В blog/views.py.

Вопрос 4.
Что попадёт в браузер, если представление содержит:
context = {"username": "Alex"}
return render(request, "blog/home.html", context) 



а шаблон содержит:
<h1>Привет, {{ username }}!</h1>
Значения из словаря context

Вопрос 5.
Чем отличаются urls.py, views.py и home.html?
views.py - отвечает за HTTP-ответы браузеру
urls.py - маршрутизация
home.html - внешний вид страницы

Практика - здесь коды всех файлов
home.html:
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>{{ title }}</h1>
        <p>{{ message }}</p>
        <a href="/about/">About blog</a>
    </body>
</html>

about.html:
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>About blog</title>
    </head>
    <body>
        <h1>About my blog</h1>
        <p>I'm studying Django here</p>
        <a href="/">Home</a>
    </body>
</html>

views.py:
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

urls.py:
from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("about/", views.about, name="about"),
    path("", views.home, name="home"),
]

🔥 Финальный вызов сенсея
Объясни своими словами, что произойдёт после того, как пользователь откроет http://127.0.0.1:8000/about/.
В ответе обязательно упомяни:
1 Как Django находит маршрут. - через path в patterns
2 Какое представление вызывается. - about.html
3 Что делает render(). - отправляет HTTP-ответ браузеру
4 Откуда берётся HTML. - из папки templates 
5 Что в итоге получает браузер. - HTML-страницу