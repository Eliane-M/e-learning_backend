from django.urls import path
from api.views.courses.courses import create_course, course_list, delete_course, update_course


urlpatterns = [
    path('', course_list, name='course_list'),
    path('new_course/', create_course, name='create_course'),
    path('delete/<int:course>/', delete_course, name='delete_course'),
    path('update/<int:course>/', update_course, name='update_course'),
]