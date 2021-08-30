from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo' : "Operaciones"
    }
    return render(request,'encuesta/formulario.html',context)
def enviar(request):
    context = {
        'titulo' : "Respuesta",
        'num1' :request.POST['num1'],
        'num2' : request.POST['num2'],
        'ope' : request.POST.getlist('ope'),
    }
    return render(request,'encuesta/respuesta.html', context)
def calcular(request):
    context = {
        'titulo' : "Clindro",
        'diametro' :request.POST['dia'],
        'altura' : request.POST['alt'],
    }
    return render(request,'encuesta/cilindro.html', context)