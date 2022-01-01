from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topic/<str:pk>/', views.Topic, name='topic'),
    path('single-news/<str:pk>/', views.singleNews, name='single-news'),

    path('create-news/', views.createNews, name='create-news'),
    path('update-news/<str:pk>/', views.updateNews, name='update-news'),
    path('delete-news/<str:pk>/', views.deleteNews, name='delete-news'),


    path('search-news/', views.searchNews, name='search-news'),


]
