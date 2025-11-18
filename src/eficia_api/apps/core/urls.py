from rest_framework import routers
from apps.empresas.views import EmpresaViewSet

router = routers.DefaultRouter()
router.register(r"empresas", EmpresaViewSet, basename="empresas")

urlpatterns = router.urls
