from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from apps.empresas.api import EmpresaViewSet
from apps.usuarios.api import UserViewSet
from apps.conceptos.api import ConceptoViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.usuarios.auth_views import MyTokenObtainPairView, me_view
from rest_framework_simplejwt.views import TokenRefreshView
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "status": "Eficia API running...",
        "version": "V.1.0.0",
        "author": "Eficia Developments SAS"
    })


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

    path('', home, name='home'),
    path('admin/', admin.site.urls),

    # API REST
    path('api/v1/', include(router.urls)),

    # AUTH JWT
    path('api/v1/auth/login/', MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/me/', me_view, name='auth_me'),

    # SWAGGER
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]
