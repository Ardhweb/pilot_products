from django.urls import path
from . import views

app_name = 'timeline'
urlpatterns = [
    path('taskadd/<int:id>/', views.anchorpoint, name='task_add'),
    path('create-task/', views.create_parent, name='create_task'),
    path('tasks/', views.parent_list, name='list_task'),
   
]
