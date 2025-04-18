"""
URL configuration for receitas_com_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# Import da função include do módulo urls
# que tem como objetivo incluir o arquivo urls 
# do nosso app na raiz do projeto.
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    
    # Rota para admins do django
    path('admin/', admin.site.urls),
    
    # Incluindo o arquivo urls.py do nosso app
    # na urls do projeto raiz. O vázio significa que 
    # não é necessário passar nenhum argumento na 
    # rota para acessar o sistema
    path('', include('receitas.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
