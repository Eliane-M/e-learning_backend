from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from models.models import Lesson
from models.serializers import LessonSerializer
from rest_framework.response import Response
from api.views.authentication.permissions.permissions import IsInstructor


@api_view(['GET'])
def get_lessons(request):
    if request.method == 'GET':
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True).data
        return Response({"Message": serializer}, status=status.HTTP_200_OK)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsInstructor])
def new_lesson(request):
    if request.method == 'POST':
        name = request.object.get('name')
        details = request.object.get('details')
        resource = request.object.get('resource')

        try:
            lesson = Lesson.objects.create(
                name=name,
                details=details,
                resource=resource,
            )
            serializer = LessonSerializer(lesson).data
            return Response({"Lesson": serializer}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)