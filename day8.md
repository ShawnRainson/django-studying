(.venv) PS D:\django-studying> cd mysite
(.venv) PS D:\django-studying\mysite> py manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0001_initial.py
    + Create model Post
(.venv) PS D:\django-studying\mysite> py manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying blog.0001_initial... OK
  Applying sessions.0001_initial... OK
(.venv) PS D:\django-studying\mysite> py manage.py showmigrations blog
blog
 [X] 0001_initial

 Задание 1 — проверка понимания
Ответь своими словами:
1 Что такое миграция Django? - изменение базы данных
2 Для чего нужна команда makemigrations? - подготовить изменения
3 Для чего нужна команда migrate? - применить изменения
4 Создаёт ли makemigrations таблицу в базе данных? - нет
5 Что хранится в файле 0001_initial.py? - инициализация миграции
6 Что означает [X] в результате showmigrations? - выполнение миграции
7 Что нужно сделать, если мы добавили новое поле в модель? - миграцию по новой
8 Почему нежелательно вручную изменять структуру базы данных? - потому-что Django изменяет её сам

Задание 2 — практическое
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    text = models.TextField()

    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    rating = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

(.venv) PS D:\django-studying\mysite> py manage.py makemigrations blog
Migrations for 'blog':
  blog\migrations\0002_post_likes.py
    + Add field likes to post
(.venv) PS D:\django-studying\mysite> py manage.py migrate blog
Operations to perform:
  Apply all migrations: blog
Running migrations:
  Applying blog.0002_post_likes... OK
(.venv) PS D:\django-studying\mysite> py manage.py showmigrations blog
blog
 [X] 0001_initial
 [X] 0002_post_likes

 Мини-вызов сенсея 🔥
Представь, что ты добавил в Post поле:
subtitle = models.CharField(max_length=200, blank=True)



А потом передумал и удалил его из models.py.

Вопрос: что нужно сделать, чтобы база данных тоже перестала содержать это поле? - выполнить миграцию

Финальный вызов
Представь, что ты работаешь в команде из трёх разработчиков.

Ты добавил новое поле в модель и создал миграцию. Твои коллеги получили обновлённый код проекта.

Вопрос: какие действия должны выполнить коллеги, чтобы их базы данных получили твоё изменение? - выполнить миграцию