🥋 Roadmap — изучение Django с нуля
🟢 Этап 1 — Знакомство с Django
🥋 День 1 — Что такое Django и первый проект
что такое Django;
зачем нужен framework;
как устроено Django-приложение;
установка Django;
виртуальное окружение;
django-admin;
startproject;
структура проекта;
manage.py;
settings.py;
urls.py;
запуск development-сервера;
runserver;
остановка сервера.

Результат: запущенный первый Django-проект.

🥋 День 2 — Django Project и Django App
что такое project;
что такое app;
зачем разделять проект на приложения;
startapp;
структура приложения;
views.py;
models.py;
admin.py;
apps.py;
migrations/;
__init__.py.

Результат: собственное приложение внутри проекта.

🥋 День 3 — URL и Views
что такое URL routing;
urls.py;
urlpatterns;
path();
views.py;
функция-view;
request;
HttpResponse;
связь:
Browser
   ↓
URL
   ↓
View
   ↓
Response
   ↓
Browser

Практика: создать несколько страниц сайта.

🥋 День 4 — Templates
зачем нужны HTML-шаблоны;
render();
передача HTML из view;
папка templates;
контекст;
{{ variable }};
{% ... %};
вывод данных в HTML.

Результат: первая динамическая HTML-страница.

🥋 День 5 — Django Template Language
переменные;
for;
if;
else;
фильтры;
with;
url;
комментарии;
работа со списками и словарями.

Практика: вывести список статей, пользователей и другие данные.

🥋 День 6 — Template inheritance
проблема повторяющегося HTML;
базовый шаблон;
{% extends %};
{% block %};
{% include %};
создание общего base.html;
навигация сайта.

Результат:

base.html
   ├── home.html
   ├── about.html
   └── profile.html
🗄️ Этап 2 — Базы данных и Models
🥋 День 7 — Что такое Model
зачем Django нужны модели;
модель как описание данных;
models.Model;
поля;
CharField;
TextField;
IntegerField;
BooleanField;
DateTimeField;
default;
null;
blank.
🥋 День 8 — Migrations
зачем нужны миграции;
makemigrations;
migrate;
0001_initial.py;
как модель превращается в таблицу;
изменение существующей модели;
почему нельзя просто менять БД вручную.

Схема:

models.py
    ↓
makemigrations
    ↓
migration
    ↓
migrate
    ↓
Database
🥋 День 9 — Django ORM
что такое ORM;
objects;
QuerySet;
all();
get();
filter();
exclude();
exists();
count();
first();
last().

Связь:

Python
   ↓
Django ORM
   ↓
SQL
   ↓
Database
🥋 День 10 — CRUD

Полный цикл работы с объектами:

Create

Post(...)
post.save()

Read

Post.objects.all()

Update

post.title = "..."
post.save()

Delete

post.delete()
🥋 День 11 — Admin
/admin/;
создание superuser;
createsuperuser;
admin.py;
admin.site.register();
управление моделями;
ModelAdmin;
list_display;
list_filter;
search_fields.

Результат: управление базой через браузер.

🔗 Этап 3 — Связи между моделями
🥋 День 12 — ForeignKey

На примере:

Author
   │
   ├── Post
   ├── Post
   └── Post
ForeignKey;
on_delete;
related_name;
один-ко-многим;
получение связанных объектов.
🥋 День 13 — OneToOneField
связь один-к-одному;
профили пользователей;
когда использовать;
отличие от ForeignKey.
🥋 День 14 — ManyToManyField

Например:

Post
 ↓
Tags
 ↓
Python
Django
Web
многие-ко-многим;
создание связей;
получение связанных объектов;
add();
remove();
clear().
🥋 День 15 — Сложные ORM-запросы
lookup;
__exact;
__contains;
__icontains;
__gt;
__gte;
__lt;
__lte;
order_by();
запросы через связи.
🥋 День 16 — Оптимизация ORM
N+1 problem;
select_related();
prefetch_related();
количество SQL-запросов;
основы оптимизации.
📝 Этап 4 — Forms
🥋 День 17 — Django Forms
зачем нужны формы;
forms.Form;
поля;
GET;
POST;
request.POST;
is_valid();
ошибки формы.
🥋 День 18 — ModelForm
ModelForm;
создание объекта через форму;
save();
редактирование;
instance;
fields.
🥋 День 19 — Валидация
validation;
clean();
clean_<field>();
собственные правила;
отображение ошибок пользователю.
🥋 День 20 — CRUD через Forms

Собираем полноценный интерфейс:

List
 ↓
Create
 ↓
Detail
 ↓
Update
 ↓
Delete
👤 Этап 5 — Пользователи
🥋 День 21 — Django User
модель пользователя;
request.user;
is_authenticated;
регистрация;
login;
logout.
🥋 День 22 — Authentication
authenticate();
login();
logout();
LoginView;
LogoutView;
login_required.
🥋 День 23 — Регистрация

Создадим:

Register
   ↓
Login
   ↓
Profile
   ↓
Logout
🥋 День 24 — Permissions
permissions;
groups;
staff;
superuser;
доступ к отдельным действиям;
права пользователей.
🎨 Этап 6 — Static и Media
🥋 День 25 — Static files
CSS;
JavaScript;
static;
STATIC_URL;
организация static-файлов;
подключение CSS к шаблонам.
🥋 День 26 — Media files
загрузка файлов;
MEDIA_ROOT;
MEDIA_URL;
ImageField;
изображения пользователей;
изображения статей.
🌐 Этап 7 — Views глубже
🥋 День 27 — Dynamic URLs
параметры URL;
<int:id>;
<slug:slug>;
передача параметров во view;
get_object_or_404().
🥋 День 28 — Function-Based Views

Глубже изучаем FBV:

request;
GET/POST;
redirect;
status codes;
обработка ошибок;
организация views.
🥋 День 29 — Class-Based Views
View;
ListView;
DetailView;
CreateView;
UpdateView;
DeleteView.

Сравним:

FBV
vs
CBV
🧩 Этап 8 — Продвинутые возможности Django
🥋 День 30 — Middleware
что такое middleware;
жизненный цикл request/response;
стандартные middleware;
собственный middleware.
🥋 День 31 — Signals
pre_save;
post_save;
pre_delete;
post_delete;
когда использовать signals;
почему иногда лучше не использовать.
🥋 День 32 — Messages и Sessions
Django messages;
sessions;
временные данные;
уведомления пользователю.
🥋 День 33 — Pagination
Paginator;
страницы;
page;
навигация;
пагинация списка статей.
🥋 День 34 — Search

Создаем поиск:

Введите запрос
      ↓
ORM
      ↓
filter()
      ↓
Результаты
🔐 Этап 9 — Безопасность
🥋 День 35 — Django Security
CSRF;
XSS;
SQL Injection;
защита форм;
пользовательский ввод;
permissions;
безопасная работа с паролями.
🚀 Этап 10 — Django REST Framework
🥋 День 36 — Что такое API
HTTP;
JSON;
REST;
endpoint;
GET;
POST;
PUT;
PATCH;
DELETE.
🥋 День 37 — DRF
установка;
serializers;
API views;
APIView;
Response.
🥋 День 38 — ViewSets и Routers
ViewSet;
ModelViewSet;
routers;
CRUD API.
🥋 День 39 — API Authentication
authentication;
permissions;
token/JWT — обзор;
защищенные endpoints.
🧪 Этап 11 — Тестирование
🥋 День 40 — Tests
зачем нужны тесты;
TestCase;
тестирование моделей;
views;
forms;
API.
🏗️ Этап 12 — Реальный проект

После изучения основных возможностей Django перестаем делать маленькие учебные примеры.

🥋 День 41+ — Большой проект

Например:

📰 Django Blog

Функциональность:

                    ┌── Register
                    │
User ───────────────┼── Login
                    │
                    └── Profile

Post
 ├── title
 ├── text
 ├── author
 ├── created_at
 ├── updated_at
 └── image

Post
 ├── Comments
 ├── Tags
 └── Likes

Будем самостоятельно реализовывать:

регистрацию;
авторизацию;
профили;
статьи;
категории;
теги;
комментарии;
лайки;
поиск;
пагинацию;
изображения;
permissions;
админку;
API;
тесты.
🎯 После курса

Финальная цель — чтобы ты мог открыть пустую директорию и самостоятельно понимать:

Что создать?
     ↓
Какую модель сделать?
     ↓
Как связать модели?
     ↓
Какой URL нужен?
     ↓
Какую View написать?
     ↓
Как получить данные через ORM?
     ↓
Как передать их в Template?
     ↓
Как принять данные из Form?
     ↓
Как авторизовать пользователя?
     ↓
Как защитить приложение?

То есть не просто знать отдельные команды Django, а понимать, как из них собирается полноценное веб-приложение.

🥋 Наша стартовая точка

И здесь важный момент: в новом плане мы начинаем с нуля, несмотря на то, что ты уже немного потрогал Django.

Поэтому завтра:

День 1 — Что такое Django и как устроен первый проект

Начнем спокойно и последовательно:

Django → установка → venv → startproject → структура проекта → manage.py → runserver.

А дальше каждый день будем двигаться по этой дорожной карте и отмечать пройденные темы ✅.

Этот план можешь спокойно сохранять в отдельный файл — это будет наша основная карта обучения Django. 🥋🐍