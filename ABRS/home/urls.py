
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('author/', views.Author.as_view()),
    path('home/add/', views.add),
]
