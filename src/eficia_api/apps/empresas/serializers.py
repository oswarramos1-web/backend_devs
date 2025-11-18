from rest_framework import serializers
from .models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"
        read_only_fields = ["usuario_creador", "fecha_creacion"]

    def validate_nit(self, value):
        if Empresa.objects.filter(nit=value).exists():
            raise serializers.ValidationError("Este NIT ya está registrado.")
        return value


def perform_create(self, serializer):
    empresa = serializer.save(usuario_creador=self.request.user)

    user = self.request.user
    if not user.empresa_default:
        user.empresa_default = empresa
        user.save()


def get_queryset(self):
    return Empresa.objects.filter(usuario_creador=self.request.user)
