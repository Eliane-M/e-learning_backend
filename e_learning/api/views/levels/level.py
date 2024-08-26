from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from models.models import Level
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from models.serializers import LevelSerializer
from api.views.authentication.permissions.permissions import IsInstructor


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsInstructor])
def new_level(request):
    name = request.data.get('name')
    if name is None:
        return Response({'message': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        level = Level.objects.create(name=name)
        serialiser = LevelSerializer(level).data
        return Response({'message': serialiser}, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)