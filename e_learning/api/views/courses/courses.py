from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from models.models import Course, Level
from models.serializers import CourseSerializer
from rest_framework.permissions import IsAuthenticated
from api.views.authentication.permissions.permissions import IsInstructor

@api_view(['GET'])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsInstructor])
def create_course(request):
    name = request.data.get('name')
    details = request.data.get('details')
    start_date = request.data.get('start_date')
    end_date = request.data.get('end_date')
    level = request.data.get('level')
    image = request.data.get('image')
    try:
        level = Level.objects.get(name__iexact=level)
    except Level.DoesNotExist:
        return Response({"error": "Level not found"}, status=status.HTTP_404_NOT_FOUND)

    if start_date and end_date:
        if start_date > end_date:
            return Response({'error': 'Start date cannot be after end date.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            duration = (f"{start_date} - {end_date}")

    if not name or details or level:
        return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        course = Course.objects.create(
            name=name,
            details=details,
            start_date=start_date,
            end_date=end_date,
            level=level,
            duration=duration,
            image=image,
        )
        serializer = CourseSerializer(course).data
        return Response({"Message": serializer}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)})
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsInstructor])
def update_course(request, course):
    if request.method == "PUT":
        name = request.data.get("name")
        description = request.data.get("description")
        if name is None:
            return Response({"message": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            course = Course.objects.get(course=int(course))
            if course is None:
                return Response({"error": "We could not find the course with that name"})
            else:
                course.name = name
                course.description = description
                course.save()
                return Response(
                    {"message": "success"},
                    status=status.HTTP_200_OK,
                )
    else:
        return Response({"message": "Failed to update the course"})
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsInstructor])
def delete_course(request, course):
    if request.method == "DELETE":
        course = Course.objects.get(course=int(course))
        if course is None:
            return Response({"error": "We could not find the course with that name"})
        else:
            course.delete()
            return Response({"message": "Course deleted successfully"})
    else:
        return Response({"message": "Failed to delete the course"})