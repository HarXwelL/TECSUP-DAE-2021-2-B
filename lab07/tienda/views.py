from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Producto 
from .models import Categoria

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    cate_list = Categoria.objects.order_by('nombre')

    request.session["nombreTienda"]="TIENDA TECH"

    context = {
        'product_list' : product_list,
        'cate_list' : cate_list
        }
    return render(request, 'index.html', context)

from tienda.carrito import Cart

def producto(request, producto_id):
    #producto = Producto.objects.get(pk=producto_id)
    producto = get_object_or_404(Producto,pk=producto_id)
    return render(request,'producto.html',{'producto':producto})

def categoria(request, categoria_id):
    cat_list = Categoria.objects.all()
    producto = Producto.objects.filter(Categoria_id = categoria_id)
    return render(request,'categoria.html',{'cat_list' : cat_list,'producto' : producto})

def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')
