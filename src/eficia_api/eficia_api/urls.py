
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from apps.empresas.api import EmpresaViewSet
from apps.usuarios.api import UserViewSet
from apps.conceptos.api import ConceptoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'empresas', EmpresaViewSet, basename='empresas')
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'conceptos', ConceptoViewSet, basename='conceptos')

schema_view = get_schema_view(
    openapi.Info(title="Eficia API", default_version='v1'),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/login/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]
