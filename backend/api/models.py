from django.db import models

# Create your models here.
class Libro(models.Model):
    codigo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    isbn = models.CharField(max_length=60)
    editorial = models.CharField(max_length=60)
    numpags =models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    numusuario = models.IntegerField(default=0)
    nif = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Prestamos(models.Model):
    idlibro = models.ForeignKey(Libro,on_delete=models.RESTRICT)
    idusuario = models.ForeignKey(Usuario,on_delete=models.RESTRICT)
    fechaPrestamo = models.DateTimeField(auto_now=True)
    fechaDevolucion = models.DateTimeField(null=True)

class Autor(models.Model):
    idlibro = models.ForeignKey(Libro,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre