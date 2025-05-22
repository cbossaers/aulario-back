from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from aulario.models import User, Aula
from aulario.serializers import UserSerializer, AulaSerializer

@permission_classes([AllowAny])
class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes([AllowAny])
class AulaList(APIView):
    """
    List all aulas, or create a new aula.
    """
    def get(self, request, format=None):
        aula = Aula.objects.all()
        serializer = AulaSerializer(aula, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AulaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([AllowAny])
class AulaDetail(APIView):
    """
    Retrieve, update or delete a aula instance.
    """
    def get_object(self, pk):
        try:
            return Aula.objects.get(pk=pk)
        except Aula.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        aula = self.get_object(pk)
        serializer = AulaSerializer(aula)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        aula = self.get_object(pk)
        serializer = AulaSerializer(aula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        aula = self.get_object(pk)
        aula.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)