🔥 Финальный вызов сенсея
Ответь своими словами на вопросы:
1 Чем отличаются {{ variable }} и {% if %}? - первое добавляет значение из словаря, второе нужно для условий
2 Для чего нужны фильтры и что делает {{ title|upper }}? - Для преобразования значений, upper нужен для того чтобы все символы были заглавными
3 Чем отличаются {% empty %} и {% else %}? - первое нужно для цикла, срабатывает если список пуст, второе нужно для if срабатывает если остальные условия не срабатывают
4 Что делает forloop.counter? - нумерует выводимые данные на странице
5 Почему список статей лучше передавать из views.py, а не прописывать каждую статью вручную в HTML? - Это удобнее, так как статей может 100 или даже 1000, и каждую прописывать долго и глупо, плючс данные могут меняться в views и автоматически изменятся на странице.

views.py:
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

home.html:
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>{{ title|title }}</h1>
        <p>{{ message }}</p>
        {% if is_published %}
           <p>Статья опубликована</p>
        {% else %}
           <p>Статья не опубликована</p>
        {% endif %}

        {% for post in posts %}
           <p>{{ post }}</p>
        {% endfor %}

        {% for i in test %}
           <p>{{ i }}</p>
        {% empty %}
           <p>List is empty</p>
        {% endfor %}

        <h1>Count of posts: {{ new_posts|length }}</h1>

        {% for post in new_posts %}
           <p>Title: {{ post.title }}, Author: {{ post.author }}</p>
           {% if post.published %}
               <p>{{ post.title }} is published</p>
            {% else %}
               <p>{{ post.title }} is not published</p>
            {% endif %}
        {% endfor %}
        <a href="/about/">About blog</a>
    </body>
</html>