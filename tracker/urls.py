from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('register/', views.register, name='register'),
    path('start/', views.start, name='start'),
    path('', views.task_list, name='task_list')
]
