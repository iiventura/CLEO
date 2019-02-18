from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='app_index'),
    #path('/about', views.about, name='app_about'),


]