from django.shortcuts import render
from .models import Noticia

def index(request):
    return render(request, 'prueba/home.html')

def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, "prueba/lista_noticias.html", {"noticias": noticias})
