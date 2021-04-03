from django.urls import path
from django.http import Http404, HttpResponseRedirect
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('del_usr/', views.del_user, name='del_usr'),
    path('home/', views.home, name='home')
]
