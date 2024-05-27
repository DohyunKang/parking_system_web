from django.urls import path
from . import views

urlpatterns = [
    path('board_list/', views.board_list, name='board_list'),
   #path('<int:pk>/', views.board_detail, name='board_detail'),
    #path('board/', views.index, name='board'),
    #path('<int:question_id>/', views.detail),
]