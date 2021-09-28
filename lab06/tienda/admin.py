from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Producto


class CategoriaAdmin(admin.ModelAdmin):
    list_disp = ('nombre','pub_date')

admin.site.register(Categoria,CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('Categoria','nombre','precio','stock')

admin.site.register(Producto,ProductoAdmin)
