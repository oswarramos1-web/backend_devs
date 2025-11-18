from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Empresa
from .serializers import EmpresaSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer

    # solo muestra empresas del usuario
    def get_queryset(self):
        return Empresa.objects.filter(usuario_creador=self.request.user)

    # asigna usuario_creador automáticamente
    def perform_create(self, serializer):
        empresa = serializer.save(usuario_creador=self.request.user)

        # si el usuario no tiene empresa_default, asignarla
        user = self.request.user
        if not user.empresa_default:
            user.empresa_default = empresa
            user.save()

    # filtros
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ["nit"]
    search_fields = ["nombre", "nit"]
    ordering_fields = ["nombre", "fecha_creacion"]
