from rest_framework import serializers
from Usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    desapegos = serializers.SlugRelatedField(many=True, read_only=True,
                                             slug_field='id')

    class Meta:
        model = Usuario
        depth = 2
        fields = (
            "fbId", "link", "username", "nome", "sobrenome", "nome_completo",
            "sexo", "amigos",
            "cadastrado", "desapegos")
