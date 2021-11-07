from django.urls import path
from .views import ShowProfilePageView, UserCreationView,UserEdit
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('register/', UserCreationView.as_view(), name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
  path('edit-profile/', UserEdit.as_view(), name='edit-profile'),
  path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show-profile')
]