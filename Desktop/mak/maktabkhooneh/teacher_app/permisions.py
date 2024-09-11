from rest_framework.permissions import BasePermission
from .models import Teacher
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        try:
            Teacher.objects.get(user = request.user)
            return True
        except:
            return False