from django.db import models


class Cuenta(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    nivel = models.IntegerField(default=1)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} {self.nombre}"
