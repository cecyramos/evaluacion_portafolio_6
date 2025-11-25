from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre