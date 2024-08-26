from rest_framework import permissions

class IsLearner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Lerner').exists()

class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Instructor').exists()