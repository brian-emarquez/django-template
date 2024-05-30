# comments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_comment/<int:post_id>/', views.add_comment_to_post, name='add_comment_to_post'),
]