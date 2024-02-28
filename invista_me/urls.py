"""
URL configuration for invista_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invista_me_app import views
from usuarios import views as usuario_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/',admin.site.urls),
    #criar um usuário
    path('conta/', usuario_views.novo_usuario, name='novo_usuario'),
    #botão de login
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name = 'login'),
    #botão de logout
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/logout.html'), name = 'logout'),
    #pagina inicial
    path('',views.pagina_inicial),
    #pagina de contato
    path('contato/',views.contato, name='contato'),
    #pagina minha historia
    path('minha_historia/',views.minha_historia, name='minha_historia'),
    #pagina para criar um novo investimento
    path('novo_investimento/',views.criar, name='novo_investimento'),
    #botão de novo investimento da lista de investimentos
    path('investimentos/',views.investimentos, name='investimentos'),
    #botão detalhe da lista de investimento
    path('investimentos/<int:id_investimento>',views.detalhe, name='detalhe'),
    #botão editar da lista de investimento
    path('novo_investimento/<int:id_investimento>',views.editar, name='editar'),
    #botão excluir da lista de investimento
    path('excluir_investimento/<int:id_investimento>',views.excluir, name='excluir')
]
