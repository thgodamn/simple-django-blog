from django.contrib import admin
from .models import Article, Comment

# Register your models here.

#добавление управления моделей Article, Comment в админку
admin.site.register(Article)
admin.site.register(Comment)
