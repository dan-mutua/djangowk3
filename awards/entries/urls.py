from django.urls import path
from django.urls import path
from django.conf.urls import include, url
from django.views.generic.edit import DeleteView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import  CreateProjectView, AddComment


urlpatterns=[
    path('', views.userhome, name='landingpage'),
    path("post/<int:pk>", views.userhome, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('profile/', views.UserProfile, name='profile' ),
    path ('profile/update/', views.EditProfile, name="update"),
    path ('entry/new/', CreateProjectView.as_view(), name="newerpost"),
    path('like/<int:pk>/', views.LikeView, name="likeproject"),
    path('post/<int:pk>/comment',AddComment.as_view(),name="comment")
]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)