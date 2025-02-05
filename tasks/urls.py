from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('', views.view_all_tasks, name='view_all_tasks'),
    path('filter/<str:priority>/', views.filter_tasks_by_priority, name='filter_tasks_by_priority'),
]