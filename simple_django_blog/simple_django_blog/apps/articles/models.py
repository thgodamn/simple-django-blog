import datetime
from django.db import models

from django.utils import timezone

# Create your models here.

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')
    #pass

    def __str__(self):
        return self.article_title

    def was_publish_risently(self):
        return self.pub_date >= (timezone.now - datetime.timedelta(days=7))

    # переименовать для админки
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)
    #pass

    def __str__(self):
        return self.author_name

    # переименовать для админки
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
