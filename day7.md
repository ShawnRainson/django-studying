Задание 1 — обязательное
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    text = models.TextField()

    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    rating = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

Задание 2 — проверка понимания
Ответь своими словами:
1 Что такое модель Django? - специальные классы Django описывающие объекты проекта
2 Для чего модель наследуется от models.Model? - для использования методов и создания полей
3 Чем CharField отличается от TextField? - первое для небольшого текста и имеет ограничения, второе для большого текста и не имеет ограничений
4 Для чего нужен max_length? - задаёт максимальное число символов
5 Что хранит BooleanField? - два значение True и False
6 Что делает default=0? - устанавливает значение по умолчанию 0
7 В чём разница между null=True и blank=True? - первое разрешает хранить NULL в базе данных, второе разрешает оставлять поля пустыми
8 Для чего нужен auto_now_add=True? - автоматическое сохранение даты и времени создания
9 Что делает метод __str__? - вохвращает поля в текстовом виде

Мини-вызов сенсея
Представь, что мы хотим добавить к статье поле likes, которое хранит количество лайков.
- Какой тип поля выберешь? - IntegerField
- Какое значение установишь по умолчанию? - 0
- Напиши одну строку кода для этого поля. - likes = models.IntegerField(default=0)

🔥 Финальный вызов
Представь, что завтра мы создаём модель Comment для комментариев к статьям.

У комментария должны быть:
- текст комментария; - TextField
- имя автора; - CharField
- количество лайков; - IntegerField
- дата создания; - DateTimeField
- статус проверки модератором. - BooleanField
Какие типы полей ты выберешь для каждого пункта?