# Import da função render do módulo django.
# shortcuts que tem como objetivo renderizar
# os nossos templates HTML
from django.shortcuts import render

# Import da função redirect do módulo django.shortcuts
# que tem como objetivo redirecionar usuários para uma
# determinada página
from django.shortcuts import redirect

# Import do formulário de cadastro de usuários
from .forms import CadastroUsuarioForm

# Import do formulário de login de usuários
from .forms import FormularioLogin

# Import do formulário de inserção de receitas

from .forms import FormularioCriacaoReceita

from django.contrib.auth import authenticate

from django.contrib.auth import login
# Create your views here.



def index(request):
    
    
    
    return render(request, 'receitas/index.html')


# Criação do método que irá criar os formulários de cadastro de usuários
# para o sistema. A função irá receber como parametro apenas o request
# que serve para lidar com requisições
def cadastroUsuario(request):
    
    # Nessa etapa vamos verificar se a requisição é do tipo POST
    # (requisição que insere dados no sistema).
    if request.method == 'POST':
        
        # Se a requisição for post, vamos instanciar o formulário
        # de cadastro e passaremos como parametro a requisição post.
        # Observação: Qualquer form ou modelform podem receber no Django
        # podem receber dados (request.post) na sua inicialização para
        # serem processados.
        form = CadastroUsuarioForm(request.POST)
        
        # Nessa etapa iremos verificar se as regras definidas pelo forms.py estão sendo seguidas corretamente.
        if form.is_valid():
            
            # Caso os dados estejam corretos, vamos salvar os dados
            user = form.save()
            
            # Após salvar os dados, iremos redirecionar o usuário 
            # para a página de login 
            return redirect('loginUsuario')
    
    else:
        
        # Caso a requisição não seja do tipo POST, iremos instanciar 
        # um formulário em branco para o usuário criar o seu cadastro
        form = CadastroUsuarioForm()
    
    # Retorno do método render com as requisições, o caminho para o
    # template e o dicionário que irá possibilitar que acessamos
    # as variáveis no template HTML
    return render(request, 'receitas/cadastroUsuario.html', {'form':form})


# View que irá criar o formulário de login do usuário
def loginUsuario(request):
    
    # Primeiro vamos verificar se a requisição é do tipo POST,
    if request.method == 'POST':
        
        # Se a requisição for do tipo POST, iremos isntanciar o
        # formulário com os valores passados pelo usuário.
        form = FormularioLogin(request.POST)
        
        # Após adquirir os valores, iremos verificar se eles estão
        # seguindo as regras definidas no forms.py
        if form.is_valid():
            
            # Se o formulário for válido, os dados limpos e validados
            # serão acessiveis através do atributo cleaned_data, que 
            # é um dicionário que irá coletar as informações dos campos
            username =form.cleaned_data['username']
            
            # faz a mesma coisa que a linha anterior, mas, coletando 
            # as senhas dos usuários.
            password = form.cleaned_data['password']
            
            # Ira realizar o login do usuário usando a requisição(POST
            # que insere dados no sistema), o username e a senha definida
            # pelo usuário no cadastro.
            user = authenticate(request, username = username, password = password)
            
            # Após realizar o login vamos verificar se a autenticação
            # funcionou 
            if user is not None: 
                
                # Se o usuário estiver autenticado (logado), iremos usar
                # a função login para criar uma sessão para esse usuário,
                # dessa maneira, as ações dele não irão afetar outros usuários.
                login(request, user)
                
                # Após realizar o login, o sistema ira direcionar o
                # usuário para a página de inserção de receitas
                return redirect ('criarReceita')
            
            else:
                
                # Esta linha adiciona um erro ao formulário. O primeiro argumento (None) indica que este é um erro não específico a um campo individual do formulário, mas sim um erro geral do formulário (como credenciais inválidas). A mensagem de erro é "Nome do usuário ou senha incorretos". Este erro será exibido ao usuário no template.
                
                form.add_error(None, "Nome do usuário ou senha incorretos")
                
                
    else:
        
        # Se a requisição não for um post, iremos instanciar um formulário # em branco para o usuário realizar o seu login.
       form = FormularioLogin()
    
    # Retorno com a renderização do template contendo a requisição,
    # o caminho do template e o dicionário que possibilitará que as
    # variáveis da view sejam acessadas no HTML
    return render(request, 'receitas/loginUsuario.html', {'form':form})
    
