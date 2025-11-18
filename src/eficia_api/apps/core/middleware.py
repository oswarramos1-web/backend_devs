from django.utils.deprecation import MiddlewareMixin
from apps.empresas.models import Empresa


class MultiEmpresaMiddleware(MiddlewareMixin):
    """
    Middleware simple: busca header X-Empresa con el ID o NIT
    y adjunta request.empresa si existe.
    """

    def process_request(self, request):
        nit = request.headers.get('X-Empresa')
        request.empresa = None
        if nit:
            try:
                request.empresa = Empresa.objects.filter(nit=nit).first()
            except Exception:
                request.empresa = None
