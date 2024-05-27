from django.urls import path, include
from . import views

app_name= 'home'

urlpatterns = [
    path('home/', views.index, name='index'),
    path('', views.before_index, name='before_index'),
]
