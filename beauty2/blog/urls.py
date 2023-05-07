from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('articles/', views.articles, name='articles'),
    path('article/<slug:slug>/', views.article, name='article'),
    path('articles/<int:page>/', views.articles, name='articles'),
]
