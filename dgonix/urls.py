"""dgonix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dgonixapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacto/', views.contacto, name='contacto'),
    path('formulario/', views.formulario, name='formulario'),
    path('hoddie/', views.hoddie, name='hoddie'),
    path('inicio-sesion/', views.inisesion, name='iniciosesion'),
    path('pantalones/', views.pantalones, name='pantalones'),
    path('poleras/', views.poleras, name='poleras'),
    path('vistaespecifica/', views.vistaesp, name='vistaespecifica'),
    path('index/', views.index, name='index'),
    path('add-cliente/', views.addCliente, name='add_cliente'),
    path('inicio', views.home, name='inicio'),
    path('', include('dgonixapp.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)