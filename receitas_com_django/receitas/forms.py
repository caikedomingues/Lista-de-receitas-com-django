

# Nessa etapa iremos definir as regras que os nossos formulários
# devem seguir.

# Importa o formulário padrão para criação de usuários.
from django.contrib.auth.forms import UserCreationForm

# Importa o modulo User padrão do django, que geralmente 
# é suficiente para informações básicas do usuário.
from django.contrib.auth.models import User

# O módulo forms da biblioteca django é uma parte fundamental do django
# para lidar com criação, exibição e validação de formulários HTML.
# Ele oferece uma maneira declarativa e estruturada de definir
# formulários em python, abstraindo muitas das complexidades do
# HTML e do processamento de dados de formulário.
# Ao importar o módulo forms dessa maneira, você torna todas as classes e funções definidas dentro desse módulo acessíveis no seu arquivo Python.
from django import forms

# Irá criar o nosso formulário de cadastro herdando os atributos
# do CreationForms. Isso ja inclui campos importantes como username
# e password
class CadastroUsuarioForm(UserCreationForm):
    
    # Classe interna para configurar o formulário 
    class Meta:
        
        # Modelo / classe que será utilizada na crição do formulário
        model = User
        
        # Campos do formulário.
        fields = ('username', 'password')




# Criação do formulário de login do usuário:  por padrão, sempre que você quiser criar um formulário que não esteja diretamente ligado a um modelo do Django no seu forms.py, você deve fazer sua classe herdar de django.forms.Form.

# django.forms.Form é a classe base para formulários genéricos no Django. Ela fornece a estrutura fundamental para definir campos de formulário, especificar widgets, adicionar validações personalizadas e processar os dados submetidos.
class FormularioLogin(forms.Form):
    
    # A nossa classe de formulário terá apenas 2 campos: username (nome
    # de usuário) e password(senha)
    
    # O username terá um rótulo chamado de "nome de usuário" e um limite
    # de 400 caracteres
    username = forms.CharField(label="Nome de Usuário", max_length=400)
    
    # O password terá um rótulo chamado de "senha" e um limite
    # de 8 caracteres
    password = forms.CharField(label="Senha", max_length=8)

