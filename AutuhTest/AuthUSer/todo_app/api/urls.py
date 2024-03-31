from django.urls import path
from todo_app.api.views import TaskListAV, TaskItemAV

urlpatterns = [
    path('list/', TaskListAV.as_view(), name= 'task-list'),
    path('<int:pk>/', TaskItemAV.as_view(), name= 'task-item'),
]