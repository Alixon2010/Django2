from django.urls import path
from todo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('<int:task_id>/edit/', views.edit, name='edit'),
    path('<int:task_id>/delete/', views.delete, name='delete'),
    path('<int:task_id>/complete/', views.complete, name='complete'),
    path('all_tasks/', views.all_tasks, name='all_tasks'),
]