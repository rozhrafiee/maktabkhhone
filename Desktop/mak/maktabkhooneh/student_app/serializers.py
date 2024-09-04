from rest_framework.serializers import ModelSerializer
from .models import Student
from class_app.serializers import ClasSerializer
from cupon_app.serializers import CuponSerializer

class StudentSerializer(ModelSerializer):
    clas = ClasSerializer(many=True)  # Include if you want to nest class details
    cupon = CuponSerializer()  # Include if you want to nest cupon details

    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_number', 'clas', 'cupon', 'wallet']
