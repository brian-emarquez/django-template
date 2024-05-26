from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/<int:id>/', views.detalle_autor, name='detalle_autor'),
]