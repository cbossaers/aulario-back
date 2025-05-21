from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from aulario.models import User
from aulario.serializers import UserSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return None