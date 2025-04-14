

# Nessa etapa iremos definir as regras que os nossos formulários
# devem seguir.

# Importa o formulário padrão para criação de usuários.
from django.contrib.auth.forms import UserCreationForm

# Importa o modulo User padrão do django, que geralmente 
# é suficiente para informações básicas do usuário.
from django.contrib.auth.models import User

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