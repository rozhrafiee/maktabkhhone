from rest_framework.permissions import BasePermission
from .models import Student

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        try:
            Student.objects.get(user = request.user)
            return True
        except:
            return False