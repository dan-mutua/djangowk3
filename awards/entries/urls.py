from django.urls import path
from django.urls import path
from django.conf.urls import include, url
from django.views.generic.edit import DeleteView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import AddCommentView, DeleteProject, FindProjectView, CreateProjectView


urlpatterns=[
    path('', views.userhome, name='landingpage'),
    path("index/", views.userhome, name='index'),
    path('profile/', views.UserProfile, name='profile' ),
    path ('profile/update/', views.EditProfile, name="update"),
    path ('entry/new/', CreateProjectView.as_view(), name="newerpost"),
    path('entry/<int:pk>/', views.FindProjectView.as_view(), name='findpost'),
    path('entry/<int:pk>/deletepost/', DeleteProject.as_view(), name='delete'),
    path('entry/<int:pk>/addcomment/', views.CommentPost, name='addcomment'),
    path('like/<int:pk>/', views.LikeView, name="likeproject"),
]



if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)