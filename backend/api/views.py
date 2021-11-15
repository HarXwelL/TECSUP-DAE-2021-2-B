from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Libro, Usuario, Prestamos, Autor
from .serializers import LibroSerializer, UsuarioSerializer, PrestamosSerializer, AutorSerializer

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({'mensaje':'Api rest de asistencia'})

@api_view(['GET'])
def libros(request):
    lstLibro = Libro.objects.all()
    serLibro = LibroSerializer(lstLibro, many=True)
    return Response(serLibro.data)

@api_view(['GET'])
def usuarios(request):
    lstUsuario = Usuario.objects.all()
    serUsuario = UsuarioSerializer(lstUsuario, many=True)
    return Response(serUsuario.data)

@api_view(['GET','POST'])
def prestamos(request):
    if request.method == 'GET':
        lstPrestamos = Prestamos.objects.all()
        serPrestamos = PrestamosSerializer(lstPrestamos, many=True)
        return Response(serPrestamos.data)
    elif request.method == 'POST':
        serPrestamos = PrestamosSerializer(data=request.data)
        if serPrestamos.is_valid():
            serPrestamos.save()
            return Response(serPrestamos.data)
        else:
            return Response(serPrestamos.errors)

@api_view(['GET'])
def autor(request):
    lstAutor = Autor.objects.all()
    serAutor=AutorSerializer(lstAutor, many=True)
    return Response(serAutor.data)
    

@api_view(['GET','PUT','DELETE'])
def prestamodetalle(request,prestamos_id):
    objPrestamos = Prestamos.objects.get(id=prestamos_id)

    if request.method == 'GET':
        serPrestamos = PrestamosSerializer(objPrestamos)
        return Response(serPrestamos.data)
    elif request.method == 'PUT':
        serPrestamos = PrestamosSerializer(objPrestamos, data=request.data)
        if serPrestamos.is_valid():
            serPrestamos.save()
            return Response(serPrestamos.data)
        else:
            return Response(serPrestamos.errors)
    elif request.method == 'DELETE':
        objPrestamos.delete()
        return Response(status=204)