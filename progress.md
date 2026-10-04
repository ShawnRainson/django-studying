🥋 День 1 — Первый Django-проект
🎯 Цели на сегодня

К концу урока ты должен понимать:

что такое Django;
что такое framework;
зачем Django нужен;
чем Django-проект отличается от приложения;
что делает django-admin;
что делает manage.py;
как создать проект;
из каких файлов состоит проект;
что находится в settings.py;
зачем нужен urls.py;
как запустить сервер;
как остановить сервер.

Сегодня не будем создавать модели, views и templates. Наша задача — понять фундамент Django и структуру проекта.

1. Что вообще такое Django?

Представь, что ты хочешь сделать веб-сайт.

Можно написать всё самостоятельно:

HTTP
↓
обработка запросов
↓
маршрутизация
↓
работа с БД
↓
авторизация
↓
HTML
↓
безопасность

Но это огромное количество работы.

Django — это веб-фреймворк для Python, который предоставляет готовую архитектуру и инструменты для создания веб-приложений.

Условно:

Python
   ↓
Django
   ↓
Web application

Django уже предоставляет механизмы для:

URL-маршрутизации;
обработки HTTP-запросов;
работы с базой данных;
HTML-шаблонов;
авторизации;
административной панели;
безопасности;
форм;
API и многого другого.

Поэтому вместо того, чтобы строить всё с нуля, мы используем готовый фундамент.

2. Что такое framework?

Framework — это каркас приложения.

Представь строительство дома.

Ты можешь:

купить землю
↓
сам спроектировать фундамент
↓
сам сделать стены
↓
сам провести электричество
↓
сам сделать канализацию

А можешь получить готовый каркас и заниматься непосредственно своим приложением.

Django примерно делает второе.

Он говорит:

«Вот тебе структура проекта, вот система URL, вот работа с БД, вот шаблоны, вот админка. Используй их и строй приложение».

3. Django-проект и Django-приложение

Это очень важное различие, поэтому запомни его с самого начала.

Project

Проект — это весь сайт/система целиком.

Например:

my_site
App

Приложение — это отдельная функциональная часть проекта.

Например:

blog
users
shop
forum

Можно представить:

                 Django Project
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
      blog          users          shop
       app            app           app

Например, у интернет-магазина:

shop_project
│
├── products
├── users
├── orders
└── payments

Это один Django project, состоящий из нескольких apps.

Пока нам достаточно понимать:

Project — весь проект. App — отдельная функциональная часть проекта.

4. Установка Django

Обычно Django устанавливают через pip.

Сначала активируем виртуальное окружение.

В Windows PowerShell:

.venv\Scripts\Activate.ps1

После этого в терминале должно появиться примерно:

(.venv) PS D:\Django\>

Теперь:

pip install django

Проверить установку можно:

django-admin --version

Если всё хорошо, увидишь версию Django.

5. django-admin

После установки появляется команда:

django-admin

Это инструмент командной строки Django.

Например, с его помощью можно создать проект:

django-admin startproject config

Здесь:

django-admin
    ↓
инструмент Django

startproject
    ↓
команда создания проекта

config
    ↓
название проекта
6. Создаём первый проект

Перейди в папку, где хочешь создать проект.

Например:

cd D:\Django

Создай проект:

django-admin startproject config

После этого появится примерно такая структура:

Django/
│
└── config/
    │
    ├── manage.py
    │
    └── config/
        │
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py

Обрати внимание на интересный момент:

config/
├── manage.py
└── config/
    ├── settings.py
    └── urls.py

Здесь две папки с одинаковым названием.

Это нормально.

Внешняя:

config/

— директория проекта.

Внутренняя:

config/

— Python-пакет с настройками проекта.

Позже мы будем давать приложениям более понятные имена, чтобы структура была нагляднее.

7. manage.py

Это один из самых важных файлов Django-проекта.

Через него мы будем выполнять множество команд:

py manage.py runserver
py manage.py startapp blog
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser

То есть:

manage.py — удобная точка управления Django-проектом из терминала.

Условно:

manage.py
    │
    ├── runserver
    ├── startapp
    ├── migrate
    ├── makemigrations
    └── createsuperuser

Не нужно запоминать все команды сейчас. Мы будем знакомиться с ними постепенно.

8. settings.py

Теперь самое интересное.

Открываем:

config/settings.py

Это главный файл настроек Django-проекта.

Там находятся настройки вроде:

SECRET_KEY = ...
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    ...
]
DATABASES = {
    ...
}
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"

Пока не нужно запоминать каждую настройку.

Главная идея:

settings.py — место, где находится конфигурация Django-проекта.

9. urls.py

Теперь:

config/urls.py

Это файл, в котором Django определяет маршруты URL.

Например:

urlpatterns = [
    path("admin/", admin.site.urls),
]

Это означает примерно:

если пользователь открыл:

/admin/

↓

Django должен обработать этот URL
через admin.site.urls

То есть:

Browser
   ↓
/admin/
   ↓
urls.py
   ↓
что делать?

Пока у нас есть только стандартный маршрут админки.

Позже мы научимся создавать:

/
 /about/
 /blog/
 /posts/
 /profile/

и связывать их с Python-кодом.

10. __init__.py

В проекте ты увидишь:

__init__.py

Пока достаточно понимать:

Это специальный файл Python, связанный с организацией директории как Python-пакета.

Сам по себе файл может быть пустым.

Не путай его с Django-миграциями.

Это пригодится нам позже, когда появится:

migrations/
    ├── __init__.py
    └── 0001_initial.py
11. asgi.py и wsgi.py

На первых этапах тебе практически не придётся с ними работать.

Их задача связана с тем, как Django-приложение взаимодействует с сервером приложений.

Пока достаточно:

asgi.py → ASGI
wsgi.py → WSGI

Не нужно сейчас заучивать, что такое ASGI и WSGI.

Мы вернёмся к этому, когда будем говорить о deployment.

12. Запускаем Django

Находясь там, где находится manage.py, выполняем:

py manage.py runserver

Django запустит development-сервер.

В терминале появится примерно:

Starting development server at http://127.0.0.1:8000/

Открываешь браузер:

127.0.0.1:8000

и увидишь стандартную страницу Django.

13. Что сейчас произошло?

Это очень важно понять.

Ты открыл:

Browser
   ↓
127.0.0.1:8000
   ↓
Django development server
   ↓
Django project
   ↓
urls.py
   ↓
ответ
   ↓
Browser

Пока мы не создавали собственную страницу.

Django просто сообщает:

«Проект успешно запущен».

14. Как остановить сервер?

В терминале, где запущен сервер, нажми:

Ctrl + C

Сервер остановится.

Это пригодится тебе постоянно.

🧠 Теперь проверяем понимание
Задание 1

Объясни своими словами:

Что такое Django?

Не надо искать официальное определение. Представь, что объясняешь другу, который знает Python, но никогда не использовал Django.

Задание 2

В чём разница между:

Django Project

и

Django App

Например:

my_site
├── blog
├── users
└── shop

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

manage.py
settings.py
urls.py
Задание 4

Что произойдёт после команды:

py manage.py runserver

Опиши цепочку от команды до появления страницы в браузере.

⌨️ Практика — создаём проект

Теперь уже работаем руками.

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
⌨️ Задача 6 — первый запуск

Запусти:

py manage.py runserver

Открой сайт в браузере.

Убедись, что появилась стандартная страница Django.

После этого останови сервер:

Ctrl + C
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

🎯 Что должно получиться после Дня 1

К концу занятия ты должен уметь самостоятельно:

установить Django
      ↓
создать project
      ↓
понимать структуру
      ↓
найти settings.py
      ↓
найти urls.py
      ↓
использовать manage.py
      ↓
запустить runserver
      ↓
остановить сервер

Сегодня не гонимся за количеством кода. Наша задача — чтобы ты понимал, что вообще происходит внутри Django.

Когда выполнишь задания, присылай свои ответы + команды/результаты из терминала, и я проверю их как сенсей: отмечу, что понял правильно, где есть пробелы, и дам следующий уровень практики. 🥋🐍

🥋 День 2 — Django Project и Django App
🎯 Цели дня

К концу урока ты должен понимать:

чем Project отличается от App;
зачем Django разделяет проект на приложения;
как создать App через startapp;
из каких файлов состоит App;
зачем нужны apps.py, models.py, views.py, admin.py;
что такое INSTALLED_APPS;
как подключить созданное приложение к проекту;
как проверить, что Django действительно увидел App.
1. 🧠 Ещё раз: Project vs App

Вчера мы определили:

Project — весь Django-проект.
App — отдельная функциональная часть проекта.

Представь интернет-магазин:

shop_project/
│
├── users/
├── products/
├── orders/
└── reviews/

Здесь:

shop_project = Project

А:

users    = App
products = App
orders   = App
reviews  = App

Каждое приложение занимается своей областью.

Например:

users
    ↓
регистрация
авторизация
профили

products
    ↓
товары
категории
цены

orders
    ↓
заказы
корзина
оплата

reviews
    ↓
отзывы
оценки
🧠 Главное

Project отвечает за весь сайт.

App отвечает за конкретную функциональность внутри сайта.

2. 🤔 Зачем вообще разделять сайт на Apps?

Представь, что мы решили написать весь сайт в одном огромном файле:

shop.py

В нём:

регистрация
товары
заказы
отзывы
корзина
админка
...

Через некоторое время получится огромная куча кода.

Django предлагает организовывать проект примерно так:

shop_project/
│
├── users/
├── products/
├── orders/
└── reviews/

Теперь каждая часть имеет своё место.

Это помогает:

организовывать код;
разделять ответственность;
повторно использовать приложения;
проще поддерживать большой проект.
3. 🥋 Создаём первый App

У тебя уже есть проект:

D:\django-studying\mysite

Перейди в него:

cd D:\django-studying\mysite

Проверь:

dir

Ты должен увидеть примерно:

manage.py
mysite/

Теперь создаём приложение.

Например, наше первое приложение назовём:

blog

Команда:

py manage.py startapp blog
Что произошло?

Django создал новую папку:

mysite/
│
├── manage.py
│
├── mysite/
│
└── blog/

То есть теперь:

mysite = Project
blog   = App
4. 🔍 Что находится внутри blog?

Выполни:

dir blog

Ты увидишь примерно:

blog/
│
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

Разберём каждый файл.

5. __init__.py
blog/
└── __init__.py

Это специальный файл Python.

Он позволяет Python воспринимать каталог как пакет.

Пока достаточно запомнить:

__init__.py → обозначает Python-пакет.

Обычно тебе практически не придётся его трогать.

6. apps.py

Внутри:

from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

Этот файл содержит конфигурацию приложения.

Например:

name = "blog"

говорит:

Это приложение называется blog.

Позже здесь могут появляться дополнительные настройки приложения.

Пока главное:

apps.py
   ↓
конфигурация App
7. models.py 🗄️

Вот этот файл будет для нас очень важным.

from django.db import models

Именно здесь мы будем создавать модели базы данных.

Например, позже:

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

Получится модель:

Post
├── title
└── text

И Django сможет связать её с таблицей базы данных.

Пока запомни:

models.py
    ↓
структура данных / модели
    ↓
база данных

До моделей мы подробно дойдём на следующих днях.

8. views.py 👀

Этот файл связан с обработкой запросов пользователя.

Например:

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello Django!")

Здесь:

def hello(request):

создаёт функцию, которая получает HTTP-запрос.

А:

return HttpResponse("Hello Django!")

возвращает ответ.

Получается:

Браузер
   ↓
HTTP request
   ↓
View
   ↓
HTTP response
   ↓
Браузер

С views.py мы подробно будем работать в Дне 3, поэтому сейчас главное понять его назначение.

views.py → логика обработки запросов и формирования ответов.

9. admin.py 🛠️

Этот файл связан с Django Admin.

Например, позже мы сможем зарегистрировать модель:

from django.contrib import admin
from .models import Post

admin.site.register(Post)

После этого модель Post появится в административной панели Django.

То есть:

admin.py
    ↓
Django Admin

Подробно админку разберём позже.

10. tests.py 🧪

Здесь располагаются тесты приложения.

Например, позже мы будем писать:

def test_something():
    ...

Тесты позволяют автоматически проверять:

«Работает ли мой код так, как я ожидаю?»

Подробно тестирование будет намного позже.

Сейчас:

tests.py
    ↓
автоматическая проверка кода
11. migrations/ 🗄️

Ты увидишь:

migrations/
└── __init__.py

Эта папка будет хранить миграции базы данных.

Например, мы создадим:

class Post(models.Model):
    title = models.CharField(max_length=200)

Django сможет создать миграцию, которая описывает изменение структуры базы данных.

Например:

0001_initial.py

Но сами миграции подробно изучим позже.

Пока:

migrations/
    ↓
история изменений структуры базы данных
12. 🧠 Собираем App целиком

Теперь у нас есть:

blog/
│
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
├── models.py
├── tests.py
└── views.py

Можно составить такую карту:

blog
│
├── models.py
│      ↓
│   данные
│
├── views.py
│      ↓
│   обработка запросов
│
├── admin.py
│      ↓
│   админка
│
├── apps.py
│      ↓
│   конфигурация App
│
├── tests.py
│      ↓
│   тесты
│
└── migrations/
       ↓
    изменения БД
13. ⚠️ Но есть одна проблема

Мы создали:

blog/

Но Django пока ещё не знает, что это приложение является частью нашего проекта.

Создать App недостаточно.

Нужно его зарегистрировать.

Для этого существует:

INSTALLED_APPS

из:

mysite/settings.py
14. INSTALLED_APPS

Открой:

mysite/settings.py

Найди:

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

Это список приложений, которые Django знает и использует в проекте.

Добавляем наше:

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "blog",
]

Теперь:

Project
   │
   ├── встроенные Django Apps
   │
   └── blog ← наше приложение
15. 🧠 Почему blog нужно добавлять в INSTALLED_APPS?

Представь, что у тебя есть телефон и приложение:

blog

Сам факт существования папки ещё не означает, что система использует приложение.

Django должен знать:

«Это приложение является частью моего проекта».

И именно:

INSTALLED_APPS

сообщает Django:

«Вот список приложений, которые используются этим проектом».

16. Можно ли назвать App как угодно?

Технически — да, но название должно быть нормальным Python-именем.

Например:

blog
users
shop
orders
products

Хорошо.

А вот:

my-super-blog

не подходит как обычное имя Python-пакета из-за -.

Также лучше давать приложениям названия, отражающие их назначение.

Например:

users

лучше, чем:

app1

Потому что через полгода ты сразу поймёшь:

users/

а:

app1/

ещё придётся вспоминать. 😄

17. Project может содержать много Apps

Например, реальный проект блога:

my_site/
│
├── manage.py
│
├── my_site/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── blog/
├── users/
├── comments/
└── notifications/

Получается:

                    PROJECT
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
      blog           users        comments
       APP             APP            APP

И это очень важная архитектурная идея Django.

18. 🧠 Важное различие

Не путай:

Django Project

и:

Django App

Например:

D:\django-studying\mysite

— это Project.

А:

D:\django-studying\mysite\blog

— это App.

При этом название может сбивать с толку:

mysite/
│
├── manage.py
│
└── mysite/

Здесь верхний mysite — корневая директория проекта, а внутренний mysite — Python-пакет с настройками проекта.

Поэтому на практике часто делают:

myproject/
│
├── manage.py
│
└── config/

или:

myproject/
│
├── manage.py
│
└── myproject/

Главное — смотреть на структуру, а не только на название папки.

🧠 Теперь проверяем понимание

Не подглядывай выше. Ответь своими словами.

Задание 1

У нас:

my_site/
│
├── blog/
├── users/
└── shop/

Что здесь Project, а что Apps?

Задание 2

Почему Django не ограничивается одним большим приложением?

Назови хотя бы две причины, почему удобно разделять проект на Apps.

Задание 3

Что делает команда:

py manage.py startapp blog

Что именно она создаёт?

Задание 4

Соедини файл и назначение:

models.py
views.py
admin.py
apps.py
tests.py

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

⌨️ Практика — теперь код пишешь ты
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

Задача 7 — подключаем App

Открой:

mysite/settings.py

Добавь:

"blog",

в INSTALLED_APPS.

После этого запусти:

py manage.py runserver

Посмотри, есть ли ошибки.

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

mysite (внешняя папка) = ?
mysite (внутренняя папка) = ?
blog = ?
manage.py = ?
🔥 Финальный челлендж дня

Представь, что через несколько дней мы строим Django Blog.

Нам нужны:

blog
users
comments

Объясни, почему логично сделать три отдельных App, а не написать всё внутри одного blog.

И главное:

Что делает INSTALLED_APPS и зачем мы добавили туда "blog"?

🥋 Главное на сегодня

Если после Дня 2 в голове останется всего одна схема, пусть будет эта:

              DJANGO PROJECT
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
      blog         users      comments
       APP           APP         APP
        │
        ├── models.py
        ├── views.py
        ├── admin.py
        ├── apps.py
        ├── tests.py
        └── migrations/

Project объединяет приложения.
App реализует конкретную часть функциональности.
INSTALLED_APPS сообщает Django, какие Apps входят в проект.

Теперь твоя очередь, ученик. Отвечай на задания 1–5, а затем покажи результат практики 6–7. 🥋

🥋 День 3 — URLs и Views
🎯 Цели дня

Сегодня ты поймёшь:

что такое URL в Django;
что такое urls.py;
что такое View;
как браузерный запрос проходит через Django;
как связать URL с View;
что такое request;
что такое HttpResponse;
почему urls.py и views.py отвечают за разные вещи;
как сделать несколько страниц;
как подключать URLs приложения к главным URLs проекта.

К концу урока у тебя будет примерно такое:

http://127.0.0.1:8000/
        ↓
      Django
        ↓
    urls.py
        ↓
      View
        ↓
 HttpResponse
        ↓
    Браузер
1. 🧠 Что вообще происходит, когда мы открываем сайт?

Допустим, ты открываешь:

http://127.0.0.1:8000/

Браузер отправляет Django запрос:

«Дай мне страницу по адресу /.»

Django должен понять:

«Какой код должен обработать этот запрос?»

И здесь появляется:

urls.py

Он занимается маршрутизацией.

Можно представить его как диспетчера:

Запрос
  ↓
urls.py
  ↓
Куда отправить запрос?
2. 🗺️ Что такое URL-маршрутизация?

Представь сайт:

127.0.0.1:8000/
127.0.0.1:8000/about/
127.0.0.1:8000/blog/
127.0.0.1:8000/contact/

У каждого URL может быть своё поведение.

Например:

/        → главная
/about/  → информация о сайте
/blog/   → список постов
/contact/ → контакты

Django должен сопоставить URL с определённым кодом.

Например:

"/about/"
    ↓
about_view()
3. 👀 Что такое View?

View — это код, который обрабатывает запрос и возвращает ответ.

Например:

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello Django!")

Здесь:

def hello(request):

это View.

А:

return HttpResponse("Hello Django!")

означает:

«Верни браузеру HTTP-ответ с текстом Hello Django!».

4. 🧠 Очень важное разделение

У нас появляются две разные задачи.

urls.py

Отвечает:

Куда направить запрос?

views.py

Отвечает:

Что сделать с запросом?

Например:

Браузер
   │
   │ GET /hello/
   ↓
urls.py
   │
   │ "hello/" → hello
   ↓
views.py
   │
   │ hello(request)
   ↓
HttpResponse("Hello Django!")
   │
   ↓
Браузер

Это одна из самых важных схем сегодняшнего дня.

5. Создаём первое View

Открой:

blog/views.py

Сейчас там примерно:

from django.shortcuts import render

Добавь:

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello Django!")

Теперь у нас есть функция:

hello

Она принимает:

request

и возвращает:

HttpResponse
6. Что такое request?

Ты увидишь такую конструкцию постоянно:

def hello(request):

request — это объект, содержащий информацию о запросе пользователя.

Например, Django может узнать из него:

какой HTTP-метод использовался;
какие параметры передали;
какие заголовки отправил браузер;
кто пользователь;
какую информацию содержит запрос.

Пока нам достаточно упрощённой модели:

request
   ↓
«Что пользователь попросил у Django?»
7. Что такое HttpResponse?

Мы написали:

return HttpResponse("Hello Django!")

HttpResponse — это HTTP-ответ.

То есть:

request
    ↓
View
    ↓
response

Например:

Запрос:
GET /hello/

Ответ:
Hello Django!

Браузер получает ответ и показывает его пользователю.

8. 🛣️ Теперь нужно связать URL с View

Создать View недостаточно.

У нас сейчас есть:

def hello(request):
    return HttpResponse("Hello Django!")

Но Django пока не знает:

«Когда пользователь откроет /hello/, нужно вызвать hello».

Для этого открываем:

mysite/urls.py

Сейчас там примерно:

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
]
9. Импортируем наше View

Добавляем:

from blog.views import hello

Получается:

from django.contrib import admin
from django.urls import path

from blog.views import hello


urlpatterns = [
    path("admin/", admin.site.urls),
]

Теперь Django знает о функции:

hello
10. Добавляем маршрут

В urlpatterns добавляем:

path("hello/", hello),

Получается:

from django.contrib import admin
from django.urls import path

from blog.views import hello


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello),
]

Теперь Django знает:

/hello/
   ↓
hello()
11. 🚀 Проверяем

Запускаем:

py manage.py runserver

Открываем:

http://127.0.0.1:8000/hello/

Должно появиться:

Hello Django!

🎉

Поздравляю.

Ты только что создал свою первую страницу Django.

12. 🧠 Разбираем path()

Мы написали:

path("hello/", hello)

У path() здесь два основных аргумента:

path(URL, VIEW)

То есть:

path("hello/", hello)

означает:

Если URL соответствует hello/, вызвать hello.

13. Почему мы пишем hello, а не hello()?

Это очень важный момент.

Правильно:

path("hello/", hello)

Неправильно:

path("hello/", hello())

Почему?

Потому что:

hello

— это ссылка на функцию.

А:

hello()

— это немедленный вызов функции.

Django нужно сказать:

«Вот функция, вызови её, когда придёт подходящий запрос».

Поэтому:

hello

а не:

hello()
14. 🔥 Сделаем ещё одну страницу

В blog/views.py:

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello Django!")


def about(request):
    return HttpResponse("This is the About page.")

Теперь в mysite/urls.py:

from django.contrib import admin
from django.urls import path

from blog.views import hello, about


urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello),
    path("about/", about),
]

Теперь у нас:

/hello/
    ↓
Hello Django!

/about/
    ↓
This is the About page.
15. 🧠 Посмотри на архитектуру

Сейчас у тебя получилось:

mysite/
│
├── manage.py
│
├── mysite/
│   ├── settings.py
│   └── urls.py
│
└── blog/
    └── views.py

Связь:

mysite/urls.py
       │
       ├── /hello/ → blog.views.hello
       │
       └── /about/ → blog.views.about
16. А если URL не существует?

Допустим, ты открываешь:

http://127.0.0.1:8000/banana/

А такого маршрута нет:

path("banana/", ...)

Django не найдёт подходящий маршрут.

В режиме разработки ты увидишь:

404

Это означает:

404 Not Found

То есть:

Django не нашёл подходящий URL.

17. 🧠 Как Django ищет маршрут?

Посмотри:

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", hello),
    path("about/", about),
]

Django проверяет маршруты.

Условно:

Запрос /hello/

↓
admin/ ? ❌
↓
hello/ ? ✅
↓
вызываем hello()

А если:

Запрос /banana/

↓
admin/ ? ❌
↓
hello/ ? ❌
↓
about/ ? ❌
↓
404
18. ⚠️ Важная деталь: порядок маршрутов

Порядок urlpatterns имеет значение.

Django проверяет маршруты сверху вниз и использует первый подходящий маршрут.

Поэтому порядок маршрутов иногда критически важен.

Мы подробнее увидим это, когда начнём работать с динамическими URL.

19. 🏗️ Почему не хранить все URL в главном urls.py?

Сейчас у нас маленький проект:

/hello/
/about/

И всё удобно.

Но представь большой проект:

/users/
/users/login/
/users/register/
/users/profile/
/blog/
/blog/posts/
/blog/posts/1/
/blog/categories/
/comments/
/comments/create/
/shop/
/shop/products/
/shop/cart/

Если записать всё в:

mysite/urls.py

файл быстро станет огромным.

Поэтому Django позволяет каждому App иметь свой urls.py.

И это очень важный следующий шаг.

20. 🧩 Создаём blog/urls.py

Django автоматически его не создаёт.

Создай файл:

blog/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── urls.py       ← создаём сами

Внутри:

from django.urls import path
from . import views


urlpatterns = [
    path("hello/", views.hello),
    path("about/", views.about),
]

Обрати внимание:

from . import views

Точка:

.

означает:

текущий пакет blog.

21. 🔗 Подключаем blog/urls.py

Теперь главный:

mysite/urls.py

Можно сделать так:

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]

Здесь появился:

include
22. Что делает include()?

Он говорит Django:

«Если запрос подходит сюда, передай дальнейшую маршрутизацию другому urls.py.»

Получается:

Главный urls.py
        │
        │ include("blog.urls")
        ↓
   blog/urls.py
        │
   ┌────┴────┐
   ↓         ↓
hello/     about/

Это позволяет каждому App управлять своими маршрутами.

23. 🧠 Теперь структура становится красивее
mysite/
│
├── manage.py
│
├── mysite/
│   ├── settings.py
│   └── urls.py
│
└── blog/
    ├── urls.py
    └── views.py

Главный urls.py:

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]

App blog:

urlpatterns = [
    path("hello/", views.hello),
    path("about/", views.about),
]
24. 🧠 Что происходит теперь?

Пользователь открывает:

/hello/

Django делает:

                    /hello/
                       ↓
                mysite/urls.py
                       ↓
              include("blog.urls")
                       ↓
                 blog/urls.py
                       ↓
                   hello/
                       ↓
                views.hello
                       ↓
             HttpResponse(...)
                       ↓
                   Браузер

Вот это одна из главных схем Django.

25. А почему path("", include(...))?

Мы написали:

path("", include("blog.urls"))

Пустая строка означает:

«Ничего не добавляй к URL на этом уровне».

Поэтому:

/hello/

переходит в:

blog/urls.py

где уже находится:

path("hello/", views.hello)

И получается:

"" + "hello/"
       ↓
   /hello/
26. Можно использовать префикс

Например:

path("blog/", include("blog.urls"))

Тогда:

/hello/

уже не будет адресом нашего View.

Нужно будет:

/blog/hello/

Потому что:

blog/ + hello/
       ↓
   blog/hello/

Это очень удобно для организации больших проектов.

🧠 Теперь проверяем понимание

Не спеши. Здесь я хочу увидеть именно твои рассуждения.

Задание 1

Объясни своими словами:

Что такое View?

Не используй официальное определение. Представь, что объясняешь другу.

Задание 2

В чём разница между:

urls.py

и:

views.py

Что делает каждый?

Задание 3

Что означает:

path("hello/", views.hello)

Разбери эту строку по частям.

Задание 4

Почему здесь:

path("hello/", views.hello)

мы пишем:

views.hello

а не:

views.hello()
Задание 5

Что произойдёт, если пользователь откроет:

http://127.0.0.1:8000/banana/

а такого маршрута нет?

⌨️ Практика — теперь код пишешь ты
Задача 6 — первое View

В:

blog/views.py

создай:

def hello(request):
    return HttpResponse("Hello Django!")

Не забудь импорт:

from django.http import HttpResponse
Задача 7 — подключаем URL

Создай:

blog/urls.py

и подключи:

from django.urls import path
from . import views


urlpatterns = [
    path("hello/", views.hello),
]

Затем подключи blog.urls в главном:

mysite/urls.py

через:

include
Задача 8 — проверка

Запусти:

py manage.py runserver

Открой:

http://127.0.0.1:8000/hello/

Ты должен увидеть:

Hello Django!
⭐ Мини-челлендж

Добавь вторую View:

about

Она должна возвращать:

This is my blog.

И сделай URL:

/about/

В итоге:

/hello/
    ↓
Hello Django!

/about/
    ↓
This is my blog.
🔥 Финальный челлендж

Не заглядывая выше, объясни весь путь запроса:

http://127.0.0.1:8000/about/

начиная с момента, когда пользователь нажал Enter в браузере, и заканчивая моментом, когда браузер получил:

This is my blog.

Постарайся рассказать примерно как цепочку:

Браузер
   ↓
?
   ↓
?
   ↓
?
   ↓
HttpResponse
   ↓
Браузер
🥋 Главная мысль Дня 3

Если сегодня запомнить только одну вещь, пусть это будет:

URL
 ↓
urls.py
 ↓
View
 ↓
Response

И ещё одно правило:

urls.py решает, КУДА направить запрос.
views.py решает, ЧТО сделать с запросом.

Сегодня твоя задача — не просто скопировать код, а самостоятельно построить эту цепочку. Именно здесь Django начинает становиться понятным. 🥋