

# Import do módulo models da biblioteca django.db.
from django.db import models

# Import da classe User do módulo django.contrib.auth.models

# Atributos: A classe User possui atributos para armazenar informações sobre os usuários, como username, password, email, first_name, last_name, is_staff, is_active, date_joined, etc. Isso está correto.

# Métodos: A classe User em si possui alguns métodos relacionados ao usuário (como get_full_name(), check_password(), set_password(), has_perm(), has_module_perms(), etc.).

from django.contrib.auth.models import User
# Create your models here.


# Nessa etapa iremos criar as classes que serão as tabelas 
# do nosso banco de dados

# Classe que será a tabela de receitas do sistema, no django
# todas as classes herdam da classe Model do módulo models
class Receitas(models.Model):
    
    # No django a criação de Colunas da tabela utilizam
    # os campos do móudlo models que contém os tipos de dados
    # de cada tabela.
    
    # O titulo da receita será do tipo texto e terá um limite de 
    # 200 caracteres
    titulo = models.CharField(max_length=200)
    
    # Os ingredientes das receitas serão do tipo texto e terá um limite de 
    # de 400 caracteres
    ingredientes = models.CharField(max_length=400)
    
    # O modo de preparo da receita será do tipo texto
    # e terá um limite de 400 caracteres
    modo_preparo = models.CharField(max_length=400)
    
    # O campo do datafield tem como objetivo pegar do sistema
    # a data em que o dado foi inserido no sistema.
    data_da_postagem = models.DateField(auto_now_add=True)
    
    # Chave estrangeira que irá relacionar essa tabela com
    # a tabela de usuários com o objetivo de associar a receita
    # a um usuário. O método Cascade permite que o sistema apague
    # todas as receitas relacionadas ao dono caso o usuário seja
    # excluido do sistema.
    dono_receita = models.ForeignKey(User, on_delete=models.CASCADE)


   

