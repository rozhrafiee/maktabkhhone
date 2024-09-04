from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView
from .models import Cupon
from .serializers import CuponSerializer
from django.http import HttpResponse

class CuponList(ListAPIView):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

class CuponDetail(RetrieveAPIView):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

class CreateCupon(CreateAPIView):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

class UpdateCupon(UpdateAPIView):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

class DeleteCupon(DestroyAPIView):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer

class CuponDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer
