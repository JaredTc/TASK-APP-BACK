from django.urls import path
from core.auth.views import LoginView
from core.users.views import UserRegistrationView, UserListView, UpdateUserView, DeleteUserView, UserInfoView

urlpatterns = [
    path('register-user/', UserRegistrationView.as_view(), name='register'),
    path('user-list/', UserListView.as_view(), name='users'),
    path('update-user/<int:pk>', UpdateUserView.as_view(), name='update-user'),
    path('delete-user/<int:pk>', DeleteUserView.as_view(), name='delete-user'),
    path('view-user/<int:pk>', UserInfoView.as_view(), name='view-user'),
]