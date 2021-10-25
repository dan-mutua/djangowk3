from .views import HomeView,EntryView
from django.urls import path

urlpatterns = [
    
    path('', HomeView.as_view(), name='homed' ),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry', ),
]
