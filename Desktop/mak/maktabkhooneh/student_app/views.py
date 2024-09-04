from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from class_app.serializers import ClasSerializer  # Import the ClasSerializer
from cupon_app.serializers import CuponSerializer  # Import the CuponSerializer

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CreateStudent(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateStudent(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ListClassesByStudent(ListAPIView):
    serializer_class = ClasSerializer

    def get_queryset(self):
        student_name = self.kwargs['student_name']
        return Clas.objects.filter(student__name=student_name)

class PaymentAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        body = request.data
        try:
            student = Student.objects.get(name=body['name_inp'])
            student.wallet += int(body['price_inp'])
            student.save()
            return Response({"message": "Payment successful"}, status=status.HTTP_200_OK)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"error": "Invalid price format"}, status=status.HTTP_400_BAD_REQUEST)
