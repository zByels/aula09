from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.inicio, name='inicio'),
    path('controlfzdvee/', views.controle, name='controle'),
    path('contas/', include("contas.urls")),
    path('', views.lista_posts, name="lista_posts"),
    path('postar/', views.postar_view, name="postar"),

]
