
from django.urls import path, include

urlpatterns = [
    path('auth/',include('core.auth.urls')),
    path('users/',include('core.users.urls')),
    path('tasks/',include('core.tasks.urls')),
]