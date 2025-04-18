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

# Função do módulo django.contrib.auth. Sua principal responsabilidade
# é verificar as credenciais de um usuário (geralmente um nome de usuário
# e uma senha) em relação aos backends de autenticação configurados no
# seu projeto Django. Essa função tenta autenticar o usuário usando cada
# backend de autenticação configurado em settings.py (na lista AUTHENTICA
# TION_BACKENDS). Ele retorna um objeto User se as credenciais forem válidas
# para algum dos backends, ou None se as credenciais forem inválidas.
from django.contrib.auth import authenticate

# Esta função tem como objetivo estabelecer uma sessão de login para
# usuários que estão autenticados. A função irá receber um objeto
# HttpRequest e um objeto User autenticado como argumentos. Ele 
# armazena o ID do usuário na sessão do usuário, marcando-o como
# logado para as requisições subsequentes.
from django.contrib.auth import login

# Import da função login_required que tem como objetivo verificar
# no sistema se há ou não um usuário logado. Caso a função não
# identifique nenhum usuário no sistema, ela irá direcionar o
# usuário para a url que for definida no settings.py
from django.contrib.auth.decorators import login_required

# Import da função que encerra a sessão do usuário e o desloga do sistema
from django.contrib.auth import logout

# Import da classe Receitas que iremos utilizar para listar
# todas as receitas cadastradas pelo usuário. A classe se encontra
# no módulo models.py do nosso app. Esse arquivo serve para criar
# todas as tabelas (classes) do nosso banco de dados.
from .models import Receitas

# Create your views here.



def index(request):
    
    receitas = Receitas.objects.all()
    
    dicionario_receitas = {'receitas':receitas}
    
    return render(request, 'receitas/index.html', dicionario_receitas)


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
    

# Ira permitir que apenas usuários autenticados acessem a página
@login_required
# Função que irá inserir receitas no banco de dados do sistema. A função
# irá receber como parametro apenas o request que lida com as requisições
def criarReceita(request):
    
    # Antes de iniciarmos qualquer ação, vamos verificar o tipo
    # de requisição feita pelo usuário.
    if request.method == 'POST':
        
        # Se a requisição for do tipo POST (requisição que insere dados
        # no sistema), vamos enviar os dados informados pro formulário.
        form = FormularioCriacaoReceita(request.POST)
            
        # Após o envio dos dados, vamos verificar se eles seguem as regras
        # definidas no forms.py
        if form.is_valid():
            
            # Como nesse caso temos que associar um usuário a criação de uma 
            # receita, vamos inserir os dados de uma maneira um pouco diferente
            # Primeiro, vamos dar  um commit=False no método save para o form
            # não enviar os dados para o banco de dados, com o objetivo de mante-los
            # apenas no formulário. Dessa maneira, teremos tempo de realizar algumas
            # validações.
            receita = form.save(commit=False)
            
            # Vamos associar a criação da receita ao usuário logado.
            receita.dono_receita = request.user
            
            # Após a associação, vamos enviar os dados para o banco de dados
            # e registrar a receita no sistema
            receita.save()
            
            # Após o envio dos dados vamos direcionar o usuário para a página
            # inicial com o objetivo dele ver todas as receitas cadastradas por
            # ele e pelas outras pessoas
            return redirect('index')
        
        else:
            
            # Se os dados não forem validos, vamos chamar a função
            # que tem como objetivo tratar e informar erros de forms
            # no sistema.
            form.add_error(None, "Falha na criação da receita")
    
    else:
        
        # Se a requisição não for um POST, vamos instanciar um formulário
        # em branco pro usuário adicionar informações.
        form = FormularioCriacaoReceita()
    
    # Iraimprimir uma mensagem acessando o nome do usuário logado.
    mensagem = f"Olá {request.user.username}"
    
    # Retorno da renderização do sistema com a requisição, a rota da 
    # página html e o dicionário que irá possibilitar o acesso das
    # variáveis no HTML.
    return render(request, 'receitas/criarReceita.html', {'form':form, 'mensagem':mensagem})



# função que irá encerrar a sessão do usuário no sistema
def logoutUsuario(request):
    
    # Basta chamarmos a função logout passando como parametro a
    # requisição de logout do usuário
    logout(request)
    
    # Após encerrar a sessão iremos direcionar o usuário para a página
    # inicial que todos os usuários (inclusive os não autenticados) podem
    # acessar livremente.
    return redirect('index')