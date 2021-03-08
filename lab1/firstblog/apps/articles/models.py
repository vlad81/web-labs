from django.db import models


class Article(models.Model):
    title = models.CharField('article name', max_length=200)
    content = models.TextField('article content')
    pub_date = models.DateTimeField('date of publishing')


class Comment(models.Model):  # CASCADE - to delete comments when related article deleted
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('author name', max_length=50)
    content = models.CharField('comment content', max_length=200)
