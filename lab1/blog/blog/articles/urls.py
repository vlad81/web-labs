from django.conf.urls import url
from django.urls import path
from django.http import Http404, HttpResponseRedirect
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_article/', views.add_article, name='add_article'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('chats/', views.chat_index, name='chat_index'),
    path('chats/<str:room_name>/', views.chat_room, name='room'),

]
