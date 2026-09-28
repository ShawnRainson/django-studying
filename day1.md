Задание 1

Объясни своими словами:

Что такое Django?

Не надо искать официальное определение. Представь, что объясняешь другу, который знает Python, но никогда не использовал Django.

Ответ: Это фреймворк. Готовый "каркас" для создания веб-приложений.

Задание 2

В чём разница между:

Django Project - Все файлы, структура

и

Django App - Отдельные части

Например:

my_site - Project
├── blog - App
├── users - App
└── shop - App

Что здесь project, а что apps?

Задание 3

Посмотри:

config/
│
├── manage.py
│
└── config/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py

Объясни назначение:

manage.py - Управление проектом
settings.py - Настройки проекта
urls.py - Маршрутизация

Задание 4

Что произойдёт после команды:

py manage.py runserver

Опиши цепочку от команды до появления страницы в браузере.

Ответ: 
1 Ввод команды
2 Django запускает сервер разработчика на устройстве
3 Переход по стандартному IP переносит на стандартную страницу Django-проекта

Задача 5

Создай новый Django-проект.

Назови его, например:

mysite

После создания покажи структуру через:

dir

и самостоятельно найди:

manage.py;
внутреннюю папку проекта;
settings.py;
urls.py.

Ответ:
(.venv) PS D:\django-studying> django-admin startproject mysite
(.venv) PS D:\django-studying> dir


    Каталог: D:\django-studying


Mode                 LastWriteTime         Length Name                
----                 -------------         ------ ----                
d-----        08.09.2026     11:14                .venv               
d-----        08.09.2026     11:27                config              
d-----        08.09.2026     11:36                mysite              
-a----        08.09.2026     11:36           4101 day1.md             
-a----        08.09.2026      8:18          11935 plan.md             
-a----        08.09.2026     11:02          14965 progress.md         
-a----        05.09.2026     10:22             67 README.md           



⌨️ Задача 6 — первый запуск

Запусти:

py manage.py runserver

Открой сайт в браузере.

Убедись, что появилась стандартная страница Django.

После этого останови сервер:

Ctrl + C

Ответ:
(.venv) PS D:\django-studying\mysite> py manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 08, 2026 - 11:39:14
Django version 6.1.1, using settings 'mysite.settings'
Starting WSGI development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.1/howto/deployment/


⭐ Задача 7 — исследовательская

Открой:

settings.py

Найди:

DEBUG = True

и:

INSTALLED_APPS = [
    ...
]

Пока ничего не изменяй.

Попробуй своими словами предположить:

1.

Что, по-твоему, означает:

DEBUG = True
2.

Почему Django хранит список:

INSTALLED_APPS

Как думаешь, зачем ему знать, какие приложения используются в проекте?

Не обязательно ответить правильно — здесь мне как раз интересно увидеть твоё предположение.

Ответ: DEBUG судя по названию связан с отладкой проекта, а INSTALLED APPS - хранит список приложений, для того чтобы Django их видел

🔥 Финальный челлендж

Представь, что ты объясняешь другу следующую структуру:

my_site/
│
├── manage.py
│
└── my_site/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    ├── wsgi.py
    └── __init__.py

Объясни одним связным рассказом, что здесь находится и для чего нужен каждый важный файл.

Не заглядывай выше в урок. Попробуй восстановить всё из памяти.

Ответ: Это Django-проект под названием my_site, файл manage-py - это основной файл для управления проектом, например для запуска. в папке my_site находятся файлы с различными параметрами проекта, settings - настройки, urls - маршрутизация и т.д.