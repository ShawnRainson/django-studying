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