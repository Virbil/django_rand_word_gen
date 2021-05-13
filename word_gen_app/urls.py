from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('rand-word', views.random_word),
    path('show-word', views.show_word),
    path('reset', views.reset),
]