from django.db import models


class PeriodoNomina(models.Model):
    inicio = models.DateField()
    fin = models.DateField()
    generado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
