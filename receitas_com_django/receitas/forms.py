

# Nessa etapa iremos definir as regras que os nossos formulários
# devem seguir.

# Importa o formulário padrão para criação de usuários.
from django.contrib.auth.forms import UserCreationForm

# Importa o modulo User padrão do django, que geralmente 
# é suficiente para informações básicas do usuário.
from django.contrib.auth.models import User

# Import da classe models (tabela) que iremos utilizar no formulário
# de criação de receitas.
from .models import Receitas


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



# Formulario de criação de novas receitas para o usuário . O formulário
# irá herdar os atributos da classe ModelForm.
# ModelForm: Serve como uma ponte poderosa e conveniente entre nossos
# modelos de dados(definidos em models.py) e a criação de formulários
# HTML para interagir com esses dados. Em essência, ele autoriza grande
# parte do processo de criação de formulários que correspondem á estrutura
# dos seus modelos.
# Aqui estão os principais propósitos e benefícios do ModelForm:
# Dado um modelo Django, o ModelForm pode inferir automaticamente os campos do formulário com base nos tipos de campos definidos no modelo (CharField, IntegerField, ForeignKey, etc.).
# Ele também aplica validações padrão com base nas restrições definidas no modelo (por exemplo, max_length, required, unique).
# Isso economiza uma quantidade significativa de código que você teria que escrever manualmente para definir cada campo do formulário e suas validações correspondentes. 
# Ele também simplifica o processo de criar ou atualizar uma instância de modelo a partir dos dados submetidos no formulário através do método save().

class FormularioCriacaoReceita(forms.ModelForm):
    
    # Classe que possibilita usar os atributos da classe herdada
    class Meta:
        
        # Classe que iremos utilizar na construção do formulário
        model = Receitas
        
        # Campos do formulário
        fields = ['titulo', 'ingredientes', 'modo_preparo', 'imagem']
        
        # Rótulos dos campos do formulário
        labels = {
            
            'titulo':'Titulo da receita',
            'ingredientes':'Ingredientes',
            'modo_preparo': 'Modo de Preparo',
            'imagem': 'Imagem da receita'
        }
        
        # Widgets: É um dicionário especial dentro da classe Meta de um
        # ModelForm. Ele permite que você especifique um widget HTML 
        # diferente do padrão para um ou mais campos do modelo. As chaves
        # destes dicionários são os nomes dos campos do seu modelo, e os
        # valores são as instâncias dos widgets do Django que você deseja
        # usar para esses campos.
        
        # forms.Textarea: é uma classe de widget fornecida pelo Django.
        # Quando você associa este widget a um campo, ele fará com que
        # este campo seja renderizado como um elemento <textarea> no
        # HTML do seu formulário, em vez do <input type="text"> padrão
        # que seria usado para um Charfield sem widget especificado.
        
        # attrs={'rows': 10, 'cols': 60}: Este é um argumento passado para o construtor de forms.Textarea. O dicionário attrs permite que você defina atributos HTML adicionais para o widget.
        
        # 'rows': 10: Define o atributo rows do <textarea> como 10, especificando a altura inicial do campo em número de linhas de texto.
        
        # 'cols': 60: Define o atributo cols do <textarea> como 60, especificando a largura inicial do campo em número de caracteres por linha.


        
        widgets = {
        
            'ingredientes': forms.Textarea(attrs={'rows': 10, 'cols': 60}),
            
            'modo_preparo': forms.Textarea(attrs={'rows': 10, 'cols': 60})
        }

