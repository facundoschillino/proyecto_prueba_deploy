from django.db import models


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    portada = models.ImageField(upload_to="fotos/noticias/", blank=True)
    pruebas_en_pdf = models.FileField(upload_to='raw/noticias', blank=True)
    video = models.FileField(upload_to='videos/noticias',blank=True)
    def __str__(self):
        return self.titulo
    