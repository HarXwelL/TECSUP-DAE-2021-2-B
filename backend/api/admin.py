from django.contrib import admin

# Register your models here.
from .models import Libro, Usuario, Prestamos, Autor

admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Prestamos)
admin.site.register(Autor)