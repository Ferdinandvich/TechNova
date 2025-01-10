from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('registrar-usuario', views.registrarUsuario, name='registrar-usuario'),
    path('logout', views.custom_logout, name='deslogar-usuario'),
    path('login', views.login, name='login'),
]
