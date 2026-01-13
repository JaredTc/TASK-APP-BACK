
from django.urls import path

from core.tasks.views import *

urlpatterns = [
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('task-list/', GetTaskView.as_view(), name='task-list'),
    path('add-category/', createCategory.as_view(), name='add-category'),
    path('add-alert/', createAlert.as_view(), name='add-alert'),
    path('add-status/', createTaskStatus.as_view(), name='add-status'),
    path('total_status/', total_status.as_view(), name='total_status'),
    path('update/<uuid:id>/', UpdateTask.as_view(), name='update-task'),

]