from rest_framework import serializers
from .models import Cine, TipoFuncion

class TipoFuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFuncion
        fields = ['id', 'nombre']

class CineSerializer(serializers.ModelSerializer):
    tipos_funcion = serializers.PrimaryKeyRelatedField(
        queryset=TipoFuncion.objects.all(),
        many=True
    )

    class Meta:
        model = Cine
        fields = ['id', 'nombre', 'ubicacion', 'tipos_funcion', 'foto_sede']