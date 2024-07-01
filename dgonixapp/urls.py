#from django.conf.urls import urls
from django.urls import path
from . import views
from .views import index


urlpatterns = [
    path('', views.home, name='inicio'),
    path('contacto', views.contacto, name='contacto'),
    path('formulario', views.formulario, name='formulario'),
    path('hoddie', views.hoddie, name='hoddie'),
    path('inicio-sesion', views.inisesion, name='iniciosesion'),
    path('pantalones', views.pantalones, name='pantalones'),
    path('poleras', views.poleras, name='poleras'),
    path('vistaespecifica', views.vistaesp, name='vistaespecifica'),
     path('', index, name='index'),
]