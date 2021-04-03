import datetime
from json import JSONEncoder

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('article name', max_length=200)
    content = models.TextField('article content')
    pub_date = models.DateTimeField('date of publishing', default=timezone.now)

    def __str__(self):
        return self.title

    def last_week_published(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):  # CASCADE - to delete comments when related article deleted
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    content = models.CharField('comment content', max_length=200)
    pub_date = models.DateTimeField('date of publishing', default=timezone.now)

    def __str__(self):
        return self.article.__str__()
