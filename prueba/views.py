from django.shortcuts import render
from .models import Foto

def index(request):
    return render(request, 'prueba/home.html')

def lista_fotos(request):
    fotos = Foto.objects.order_by("-creado")
    return render(request, "prueba/lista_fotos.html", {"fotos": fotos})
