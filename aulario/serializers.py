from rest_framework import serializers
from aulario.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'admin')


class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = ('id', 'name', 'capacity')


class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('id', 'code', 'name')


class CursoSerializer(serializers.ModelSerializer):
    asignaturas = AsignaturaSerializer(many=True, read_only=True)
    asignaturas_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Asignatura.objects.all(),
        write_only=True,
        source='asignaturas'
    )

    class Meta:
        model = Curso
        fields = ['id', 'name', 'capacity', 'asignaturas', 'asignaturas_ids']


def create(self, validated_data):
        asignaturas = validated_data.pop('asignaturas')
        curso = Curso.objects.create(**validated_data)
        curso.asignaturas.set(asignaturas)
        return curso

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('id', 'name', 'aula', 'curso', 'asignatura', 'usuario', 'fecha')
