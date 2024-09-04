from rest_framework.serializers import ModelSerializer
from .models import Teacher
from class_app.serializers import ClasSerializer  

class TeacherSerializer(ModelSerializer):
    clas = ClasSerializer(many=True)  

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'clas', 'rate', 'wallet']
