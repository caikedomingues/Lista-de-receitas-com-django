
# Irá servir para acessar as rotas das nossas views no djnago
from django.urls import path

# Import do arquivo view que esta aqui na pasta do nosso app,
# usaremos a views para fazer referencia a página que a rota 
# deverá acessar.
from . import views

urlpatterns = [
    
    # Criando a rota para a view da página inicial
    # que irá conter todas as receitas criadas pelos
    # usuários.
    path('', views.index, name='index'),
    
    # Criando a rota para a view de cadstro de usuários 
    # no sistema.
    path('cadastroUsuario', views.cadastroUsuario, name='cadastroUsuario'),
    
    # Criação da rota para a página de login.
    path('login', views.login, name='login')
    
]