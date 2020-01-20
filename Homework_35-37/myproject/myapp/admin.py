from django.contrib import admin
from .models import Article, Comment, Like, Author, Blog

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('Comment', 'Date')

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Author)
admin.site.register(Blog)