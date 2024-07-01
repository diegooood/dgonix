#from django.conf.urls import urls
from django.urls import path
from . import views
from .views import index
from django.contrib.auth import views as auth_views
from .views import login_view, logout_view, home_view

urlpatterns = [
    path('', views.home, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    path('formulario', views.formulario, name='formulario'),
    path('hoddie', views.hoddie, name='hoddie'),
    path('inicio-sesion', views.inisesion, name='iniciosesion'),
    path('pantalones', views.pantalones, name='pantalones'),
    path('poleras', views.poleras, name='poleras'),
    path('vistaespecifica', views.vistaesp, name='vistaespecifica'),
    path('index/', views.index, name='index'),
    path('add-cliente/', views.addCliente, name='add_cliente'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', home_view, name='home'),
    
]