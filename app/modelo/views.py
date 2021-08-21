from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("SUMAS")
def suma(request):
    return HttpResponse("SUMA DE DIGITOS")
def num1(request, num1):
    response = "Los numeros son %s"
    return HttpResponse(response % num1) 
def num2(request, num1, num2):
    resp = "Los numeros son %a"
    return HttpResponse(resp % num2) 
def votar(request, num1, num2):
    suma = int(num1) + int(num2)
    respuesta = "LA RESPUESTA ES: " + str(suma)
    return HttpResponse(respuesta)

