from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nViews: {self.views}\n"
