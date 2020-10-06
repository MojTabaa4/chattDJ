from django.urls import path
from .views import LoginView, SignupView, ProfileView, UserListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('userlist/', UserListView.as_view(), name='user-list'),
]
