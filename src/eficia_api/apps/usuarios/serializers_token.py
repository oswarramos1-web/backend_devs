# apps/usuarios/serializers_token.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Extiende el token para devolver datos del usuario y la empresa por defecto.
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Claims custom (si quieres)
        token['username'] = user.username
        token['email'] = user.email
        # incluir empresa_default id si existe
        empresa_id = getattr(user, 'empresa_default_id', None)
        if empresa_id:
            token['empresa_id'] = empresa_id
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # Agregar información del usuario en la respuesta junto con tokens
        data.update({
            'user': {
                'id': self.user.id,
                'username': self.user.username,
                'email': self.user.email,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
                'empresa_default': getattr(self.user, 'empresa_default_id', None)
            }
        })
        return data
