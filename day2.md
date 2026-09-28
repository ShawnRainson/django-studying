Задание 1

У нас:

my_site/ - Project
│
├── blog/ - App
├── users/ - App
└── shop/ - App

Что здесь Project, а что Apps?

Задание 2

Почему Django не ограничивается одним большим приложением?

Назови хотя бы две причины, почему удобно разделять проект на Apps.
1 Читаемость кода лучше
2 Удобное разделение на функциональные части

Задание 3

Что делает команда:

py manage.py startapp blog

Что именно она создаёт?
Ответ: она создаёт папку приложения blog

Задание 4

Соедини файл и назначение:

models.py - B
views.py - D
admin.py - E
apps.py - A
tests.py - C

с:

A. Конфигурация приложения
B. Модели и структура данных
C. Тесты
D. Обработка запросов
E. Работа с Django Admin

Задание 5

Мы создали:

blog/

Но забыли добавить:

"blog",

в:

INSTALLED_APPS

Как ты думаешь, почему это может стать проблемой?
Ответ: Django не увидит новое созданное приложение

Задача 6 — создаём App

В своём проекте:

D:\django-studying\mysite

выполни:

py manage.py startapp blog

Затем:

dir

и:

dir blog

Посмотри, что создал Django.

Ответ:
(.venv) PS D:\django-studying\mysite> py manage.py startapp blog
(.venv) PS D:\django-studying\mysite> cd blog
(.venv) PS D:\django-studying\mysite\blog> dir


    Каталог: D:\django-studying\mysite\blog


Mode                 LastWriteTime         Length Name                
----                 -------------         ------ ----                
d-----        28.09.2026      7:53                migrations          
-a----        28.09.2026      7:53             66 admin.py            
-a----        28.09.2026      7:53             88 apps.py             
-a----        28.09.2026      7:53             60 models.py           
-a----        28.09.2026      7:53             63 tests.py            
-a----        28.09.2026      7:53             66 views.py            
-a----        28.09.2026      7:53              0 __init__.py         


Задача 7 — подключаем App

Открой:

mysite/settings.py

Добавь:

"blog",

в INSTALLED_APPS.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

После этого запусти:

py manage.py runserver

Посмотри, есть ли ошибки.
Результат:
(.venv) PS D:\django-studying\mysite> py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 28, 2026 - 08:16:41
Django version 6.1.1, using settings 'mysite.settings'
Starting WSGI development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.1/howto/deployment/


⭐ Мини-челлендж

Не копируя из урока, нарисуй структуру своего проекта примерно так:

mysite/
│
├── manage.py
│
├── mysite/
│
└── blog/

И рядом подпиши:

mysite (внешняя папка) = Главная папка проекта
mysite (внутренняя папка) = Пакет с настройками
blog = Приложение
manage.py = Файл для управления проектом

🔥 Финальный челлендж дня

Представь, что через несколько дней мы строим Django Blog.

Нам нужны:

blog
users
comments

Объясни, почему логично сделать три отдельных App, а не написать всё внутри одного blog.
Ответ: Чтобы не делать громоздкий код, а разделить его на отдельные и понятные функциональные элементы

И главное:

Что делает INSTALLED_APPS и зачем мы добавили туда "blog"?
Ответ: INSTALLED_APPS нужен для установки новых приложений проекта, он говорит Django: "Вот новое приложение в нашем проекте"