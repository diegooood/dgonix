from django.db import models

# Create your models here.

class Formulario(models.Model):
    nombre = models.CharField( max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)
    numero = models.CharField(max_length=12)
    rut = models.CharField(primary_key=True,max_length=10)
    contrasena = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.correo}'