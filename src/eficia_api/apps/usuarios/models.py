from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    nit = models.CharField(max_length=50, blank=True, null=True)  # opcional
    empresa_default = models.ForeignKey(
        "empresas.Empresa",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="usuarios_default"
    )

    def __str__(self):
        return self.email or self.username
