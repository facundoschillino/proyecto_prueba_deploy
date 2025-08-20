from django.db import models

class Foto(models.Model):
    titulo = models.CharField(max_length=120)
    imagen = models.ImageField(upload_to="fotos/")  # Se guarda en Cloudinary
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

