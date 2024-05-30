# profiles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('<int:pk>/', views.profile_detail, name='profile_detail'),
]