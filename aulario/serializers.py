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
    asignaturas = AsignaturaSerializer(many=True)


    class Meta:
        model = Curso
        fields = ('id', 'name', 'capacity', 'asignaturas')


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('id', 'name', 'aula', 'curso', 'asignatura', 'usuario', 'fecha')
