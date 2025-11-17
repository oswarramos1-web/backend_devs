from rest_framework import serializers
from .models import Concepto


class ConceptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concepto
        fields = ['id', 'codigo', 'nombre', 'descripcion',
                  'es_porcentaje', 'valor', 'activo', 'created_at']
        read_only_fields = ['created_at']
