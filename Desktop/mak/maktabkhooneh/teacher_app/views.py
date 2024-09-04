from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from .serializers import TeacherSerializer

class TeacherList(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CreateTeacher(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class UpdateTeacher(UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class DeleteTeacher(DestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class AverageRateAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        all_teachers = Teacher.objects.all()
        if not all_teachers:
            return Response({"average_rate": 0}, status=status.HTTP_200_OK)
        total_rate = sum(teacher.rate for teacher in all_teachers)
        average = total_rate / len(all_teachers)
        return Response({"average_rate": average}, status=status.HTTP_200_OK)

class SortByRateAPIView(ListAPIView):
    def get(self, request, *args, **kwargs):
        sorted_list = Teacher.objects.all().order_by('-rate')
        serializer = TeacherSerializer(sorted_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
