from django.db import models
from django.utils import timezone
from _datetime import timedelta
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Comment(models.Model):
    article_name = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.text}"

    def save(self, **kwargs):
        if not self.id:
            dt = timezone.now()
            dt = dt.replace(year=dt.year - 1)
            self.date = dt
            super().save(**kwargs)

class Blog(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class Like(models.Model):
    article_name = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
