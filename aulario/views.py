from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from aulario.models import User, Aula, Asignatura, Curso, Reserva
from aulario.serializers import (UserSerializer, AulaSerializer, AsignaturaSerializer,
                                 CursoSerializer, ReservaSerializer)


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


@permission_classes([AllowAny])
class AsignaturaList(APIView):
    """
    List all asignaturas, or create a new asignatura.
    """

    def get(self, request, format=None):
        asignatura = Asignatura.objects.all()
        serializer = AsignaturaSerializer(asignatura, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AsignaturaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class AsignaturaDetail(APIView):
    """
    Retrieve, update or delete a asignatura instance.
    """

    def get_object(self, pk):
        try:
            return Asignatura.objects.get(pk=pk)
        except Asignatura.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        asignatura = self.get_object(pk)
        serializer = AsignaturaSerializer(asignatura)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        asignatura = self.get_object(pk)
        serializer = AsignaturaSerializer(asignatura, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        asignatura = self.get_object(pk)
        asignatura.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([AllowAny])
class CursoList(APIView):
    """
    List all curso, or create a new curso.
    """

    def get(self, request, format=None):
        curso = Curso.objects.all()
        serializer = CursoSerializer(curso, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class CursoDetail(APIView):
    """
    Retrieve, update or delete a curso instance.
    """

    def get_object(self, pk):
        try:
            return Curso.objects.get(pk=pk)
        except Curso.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        curso = self.get_object(pk)
        serializer = CursoSerializer(curso)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        curso = self.get_object(pk)
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        curso = self.get_object(pk)
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@permission_classes([AllowAny])
class ReservaList(APIView):
    """
    List all reserva, or create a new reserva.
    """

    def get(self, request, format=None):
        reserva = Reserva.objects.select_related('aula', 'curso', 'asignatura', 'usuario').all()
        serializer = ReservaSerializer(reserva, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class ReservaDetail(APIView):
    """
    Retrieve, update or delete a reserva instance.
    """

    def get_object(self, pk):
        try:
            return Reserva.objects.select_related('aula', 'curso', 'asignatura', 'usuario').get(pk=pk)
        except Reserva.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reserva = self.get_object(pk)
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        reserva = self.get_object(pk)
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        reserva = self.get_object(pk)
        reserva.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
