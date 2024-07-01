from django.shortcuts import render
from .models import Formulario
from django.db import IntegrityError

# Create your views here.

def home(request):
    return render(request, 'dgonixapp/inicio.html')

def contacto(request):
    return render(request, 'dgonixapp/contacto.html')

def formulario(request):
    return render(request, 'dgonixapp/formulario.html')

def hoddie(request):
    return render(request, 'dgonixapp/hoddie.html')

def inisesion(request):
    return render(request, 'dgonixapp/iniciosesion.html')

def pantalones(request):
    return render(request, 'dgonixapp/pantalones.html')

def poleras(request):
    return render(request, 'dgonixapp/poleras.html')

def vistaesp(request):
    return render(request, 'dgonixapp/vistaespecifica.html')

def index(request):
    formularios = Formulario.objects.all()
    print(f'Formularios: {formularios}')
    context = {"formularios":formularios}
    return render(request, 'formulario.html', context)

def addCliente(request):
    if request.method == 'GET':

        return render(request,'formulario.html')
    else:
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        numero = request.POST.get('numero')
        rut = request.POST.get('rut')
        contrasena = request.POST.get('contrasena')

        try:
            formularios = Formulario.objects.create(
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                numero=numero,
                rut=rut,
                contrasena=contrasena,
                activo=True
            )
            return render(request, 'formulario.html')
        except IntegrityError:
            mensaje_error = ""
            return render(request, 'formulario.html', {'mensaje_error': mensaje_error})










