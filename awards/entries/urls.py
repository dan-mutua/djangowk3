from .views import HomeView,EntryView,CreateView
from django.urls import path

urlpatterns = [
    
    path('', HomeView.as_view(), name='homed' ),
    path('entry/<int:pk>/', EntryView.as_view(), name='entrydetail', ),
    path('create/',CreateView.as_view(), name='create'),
]
