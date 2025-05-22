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