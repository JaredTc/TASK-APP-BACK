from django.urls import path, include
from core.auth.views import LoginView

urlpatterns = [
    path('auth-user/', LoginView.as_view(), name='login'),
]