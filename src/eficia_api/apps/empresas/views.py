from rest_framework import viewsets, permissions
from .models import Empresa
from .serializers import EmpresaSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo las empresas del usuario autenticado
        return Empresa.objects.filter(usuario_creador=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario_creador=self.request.user)
