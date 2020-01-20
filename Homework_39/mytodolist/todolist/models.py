from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Author(User):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Note(models.Model):

    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creation_date"] #ordering by the created field

    def __str__(self):
        return self.title #name to be shown when called