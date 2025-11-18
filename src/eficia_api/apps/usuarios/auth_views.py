# apps/usuarios/auth_views.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers_token import MyTokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me_view(request):
    """Devuelve datos del usuario actual (útil para front)."""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
