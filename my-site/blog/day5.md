🥋 Практика — теория
Задание 1

Объясни своими словами разницу между:

py manage.py makemigrations

и:

py manage.py migrate

Ответ: Первое это подготовка к миграции, второе сама миграция

Задание 2

Что произойдет?

post = Post(
    title="Python",
    author="Shawn"
)

А затем:

post.save()

Почему необходим save()?

Ответ: Это создание новой статьи, а save необходимо для сохранения.

Задание 3

Что вернут эти запросы?

Post.objects.all()
Post.objects.filter(author="Shawn")
Post.objects.get(id=5)

Объясни разницу между ними.

Ответ: all - вернёт все поля, filter - отфильтрует по автору "Shawn", а get - вернёт по id = 1

Задание 4

Почему ORM можно представить следующим образом?

Python → ORM → SQL → Database

Что делает ORM?

Ответ: ORM даёт команды Django, а тот в свою очередь превращает их в SQL-запрос который идёт в базу

⌨️ Практика — код

Теперь работаем с твоей моделью Post.

Она у тебя уже есть:

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    views = models.IntegerField(default=0)

Задача 5 — миграции

Выполни:

py manage.py makemigrations

затем:

py manage.py migrate

После этого посмотри, что изменилось в папке:

blog/migrations/

Обрати внимание, какой файл появился.

Ответ:
__init__.py

Задача 6 — создаём статьи

Создай несколько объектов Post.

Например, в Django shell:

py manage.py shell

Внутри shell импортируй модель:

from blog.models import Post

Создай минимум три статьи.

У каждой должны быть разные:

title;
author;
views.

Сохрани их через .save().

Задача 7 — читаем базу

После создания попробуй самостоятельно выполнить:

Post.objects.all()

Потом:

Post.objects.filter(author="...")

И:

Post.objects.get(id=1)

Посмотри, что возвращает каждый запрос.

Ответ:
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>, <Post: Post object (2)>, <Post: Post object (3)>]>
>>> Post.objects.filter(author="Mia")
<QuerySet [<Post: Post object (2)>]>
>>> Post.objects.get(id=2)
<Post: Post object (2)>
>>> 

⭐ Мини-челлендж

Попробуй самостоятельно сделать следующее:

Получить статью с id=1.
Изменить количество просмотров.
Сохранить изменение.
Снова получить статью.
Убедиться, что значение изменилось.

Подсказка:

post = ...
post.views = ...
post.save()

Ответ:
>>> post = Post.objects.get(id=1)
>>> post.views = 4
>>> post.save()
>>> Post.objects.get(id=1)
<Post: Title: Django studying
Author: Shawn
Views: 4>
>>> 

🥋 Сенсейский вопрос

Представь:

post = Post(
    title="Django",
    author="Shawn"
)

В какой момент статья реально появляется в базе данных?

И почему:

post = Post(...)

и

post.save()

— это не одно и то же?

Ответ: post = Post(...) - это создание параметров объекта, а save() - это уже сохранение в базе.

⭐ Дополнительный вызов

Представь, что ты сделал:

Post.objects.filter(author="Shawn")

и получил 10 статей.

Как думаешь, почему здесь используется filter(), а не get()?

Ответ: get() - нужен для поиска одной статьи по id, а filter для вывода нескольких статей по какому-либо параметру

⭐ Финальный челлендж Дня 5

Не просто добавь __str__, а попробуй самостоятельно ответить:

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    views = models.IntegerField(default=0)

    def __str__(self):
        ...

Что должно находиться вместо ..., чтобы Post.objects.all() показывал название статьи вместо Post object (1)?

И второй вопрос:

Почему здесь вообще работает return self.title? Что такое self в данном случае?

Ответ 1:
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nViews: {self.views}\n"

Ответ 2:
return работает потому-что мы возвращем значения полей, а self работает потому что мы обращаемся к полям класса Post