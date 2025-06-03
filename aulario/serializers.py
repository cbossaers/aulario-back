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
    aula = AulaSerializer(read_only=True)
    curso = CursoSerializer(read_only=True)
    asignatura = AsignaturaSerializer(read_only=True)
    usuario = UserSerializer(read_only=True)

    # Campos para escritura
    aula_id = serializers.PrimaryKeyRelatedField(
        queryset=Aula.objects.all(),
        write_only=True,
        source='aula'
    )
    curso_id = serializers.PrimaryKeyRelatedField(
        queryset=Curso.objects.all(),
        write_only=True,
        source='curso'
    )
    asignatura_id = serializers.PrimaryKeyRelatedField(
        queryset=Asignatura.objects.all(),
        write_only=True,
        source='asignatura'
    )
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='usuario'
    )

    class Meta:
        model = Reserva
        fields = ['id', 'name', 'fecha',
                  'aula', 'aula_id',
                  'curso', 'curso_id',
                  'asignatura', 'asignatura_id',
                  'usuario', 'usuario_id']

    def create(self, validated_data):
        return Reserva.objects.create(**validated_data)
