from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    fecha_estreno = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo