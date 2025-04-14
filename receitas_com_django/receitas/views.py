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
            return redirect('login')
    
    else:
        
        # Caso a requisição não seja do tipo POST, iremos instanciar 
        # um formulário em branco para o usuário criar o seu cadastro
        form = CadastroUsuarioForm()
    
    # Retorno do método render com as requisições, o caminho para o
    # template e o dicionário que irá possibilitar que acessamos
    # as variáveis no template HTML
    return render(request, 'receitas/cadastroUsuario.html', {'form':form})



def login(request):
    
    
    
    return render(request, 'receitas/login.html')
    
    