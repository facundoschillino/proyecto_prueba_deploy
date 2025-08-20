from django.urls import path
from .views import index, lista_fotos

urlpatterns = [
    path('', index, name='home'),
    path("fotos/", lista_fotos, name="lista_fotos"),
]