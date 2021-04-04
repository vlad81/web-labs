from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.index, name='index'),
    path('doc/', views.doc, name='doc'),
    path('openapi.json', views.openapi, name='openapi')
]
