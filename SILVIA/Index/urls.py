from django.urls import path
from . import views

urlpatterns = [
    path('login', views.index, name='app_index'),
]