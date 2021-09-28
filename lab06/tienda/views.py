from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Producto 
from .models import Categoria

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    cate_list = Categoria.objects.order_by('nombre')
    context = {
        'product_list' : product_list,
        'cate_list' : cate_list
        }
    return render(request, 'index.html', context)

def producto(request, producto_id):
    #producto = Producto.objects.get(pk=producto_id)
    producto = get_object_or_404(Producto,pk=producto_id)
    return render(request,'producto.html',{'producto':producto})

def categoria(request, categoria_id):
    cat_list = Categoria.objects.all()
    producto = Producto.objects.filter(Categoria_id = categoria_id)
    return render(request,'categoria.html',{'cat_list' : cat_list,'producto' : producto})
