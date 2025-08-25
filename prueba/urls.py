from django.urls import path
from .views import index, lista_noticias

urlpatterns = [
    path('', index, name='home'),
    path("noticias/", lista_noticias, name="lista_noticias"),
]