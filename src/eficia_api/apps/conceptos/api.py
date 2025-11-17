from rest_framework import viewsets, permissions
from .models import Concepto
from .serializers import ConceptoSerializer


class ConceptoViewSet(viewsets.ModelViewSet):
    queryset = Concepto.objects.all().order_by('codigo')
    serializer_class = ConceptoSerializer
    permission_classes = [permissions.IsAuthenticated]
