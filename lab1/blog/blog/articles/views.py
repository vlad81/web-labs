import json

from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.http import Http404, JsonResponse
from django.utils import timezone

from .models import Article


def index(request):
    latest_articles_lists = Article.objects.order_by('-pub_date')[:5]

    articles = {}

    for article in latest_articles_lists:
        articles[article.id] = {
            "title": article.title,
            "author_name": User.objects.get(id=article.author.id).username,
            "article_content": article.content,
            "pub_date": json.dumps(article.pub_date, cls=DjangoJSONEncoder)
        }

    dump = {"latest_articles_list": articles}
    return JsonResponse(dump, safe=False)


def detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        raise Http404("Article not found")

    latest_comments_list = article.comment_set.order_by('-id')[:10]

    comments = {}

    for comment in latest_comments_list:
        comments[comment.id] = {
            "content": comment.content,
            "author_name": comment.author,
            "pub_date": json.dumps(comment.pub_date, cls=DjangoJSONEncoder)
        }

    data = {
        'article_title': article.title,
        'article_author': User.objects.get(id=article.author.id).username,
        'article_content': article.content,
        'latest_comments_list': comments
    }

    return JsonResponse(data, safe=False)


def leave_comment(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        return Http404("Article not found")

    if request.method == 'GET':
        comment_text = request.GET['comment_text']
        article.comment_set.create(author=request.user, content=comment_text)
        data = {
            'article_id': article_id,
            'comment_created': True
        }
        dump = json.dumps(data)
        return JsonResponse(dump, safe=False)
    else:
        return Http404('Invalid request type!')


def add_article(request):
    if request.user.is_authenticated:
        article = Article.objects.create(author=request.user, title=request.GET.get("title", "No title"),
                                         content=request.GET.get("content", "Empty"), pub_date=timezone.now())
        article.save()
        data = {
            'article_id': article.id,
            'article_created': True
        }
    else:
        data = {
            'error': "Non-logged user."
        }

    return JsonResponse(data, safe=False)
