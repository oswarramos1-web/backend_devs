from django.db import models


class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=50, unique=True)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.nit})"
