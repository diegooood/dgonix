from django.shortcuts import render, redirect
from .models import Formulario
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Formulario

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
    context = {"formularios": formularios}
    return render(request, 'dgonixapp/formulario.html', context)

def addCliente(request):
    if request.method == 'GET':
        return render(request, 'dgonixapp/formulario.html')
    elif request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        numero = request.POST.get('celular')
        rut = request.POST.get('rut')
        contrasena = request.POST.get('contrasena')

        try:
            # Crear una nueva instancia de Formulario y guardarla en la base de datos
            Formulario.objects.create(
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                numero=numero,
                rut=rut,
                contrasena=contrasena,
            )
            # Redirigir a una nueva URL después de agregar exitosamente
            return redirect('index')  # Redirige a la vista index después de guardar exitosamente
        except IntegrityError:
            # Manejo de errores por integridad de la base de datos (por ejemplo, rut duplicado)
            mensaje_error = "Error: El Rut ya existe en la base de datos."
            return render(request, 'dgonixapp/formulario.html', {'mensaje_error': mensaje_error})

    return render(request, 'dgonixapp/formulario.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
          
            try:
                formulario = Formulario.objects.get(usuario=user) 
                nombre_usuario = formulario.nombre_usuario
                request.session['nombre_usuario'] = nombre_usuario
            except Formulario.DoesNotExist:
                nombre_usuario = user.username 

            return redirect('home') 
        else:
            messages.error(request, 'Usuario o contraseña no válidos.')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    if 'nombre_usuario' in request.session:
        del request.session['nombre_usuario']  
    return redirect('home')

def home_view(request):
    return render(request, 'inicio.html')