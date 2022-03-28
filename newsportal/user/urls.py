from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('profile/<str:pk>/', views.profile, name='profile'),
    path('account/', views.userAccount, name='account'),

    path('edit-account/', views.editAccount, name='edit-account'),

    path('create-interest/', views.createInterest, name='create-interest'),
    path('edit-interest/<str:pk>/', views.updateInterest, name='edit-interest'),
    path('delete-interest/<str:pk>/', views.deleteInterest, name='delete-interest'),

    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),
]

