
# Irá servir para acessar as rotas das nossas views no djnago
from django.urls import path

# Import do arquivo view que esta aqui na pasta do nosso app,
# usaremos a views para fazer referencia a página que a rota 
# deverá acessar.
from . import views

urlpatterns = [
    
    # Criando a rota para a view da página inicial
    # que irá conter todas as receitas criadas pelos
    # usuários. Se a rota estiver vázia, ou seja, sem
    # nenhum argumento após a barra, ela irá automaticamente
    # para a página inicial
    path('', views.index, name='index'),
    
    # Criando a rota para a view de cadstro de usuários 
    # no sistema.
    path('cadastroUsuario', views.cadastroUsuario, name='cadastroUsuario'),
    
    # Criação da rota para a página de login.
    path('loginUsuario', views.loginUsuario, name='loginUsuario'),
    
    path('criarReceita', views.criarReceita, name='criarReceita'),
    
    path('logoutUsuario', views.logoutUsuario, name='logoutUsuario')
    
]