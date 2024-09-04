from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView
from .models import Factor
from .serializers import FactorSerializer
from cupon_app.models import Cupon
from django.http import HttpResponse

class FactorList(ListAPIView):
    queryset = Factor.objects.all()
    serializer_class = FactorSerializer

class FactorDetail(RetrieveAPIView):
    queryset = Factor.objects.all()
    serializer_class = FactorSerializer

class CreateFactor(CreateAPIView):
    queryset = Factor.objects.all()
    serializer_class = FactorSerializer

class UpdateFactor(UpdateAPIView):
    queryset = Factor.objects.all()
    serializer_class = FactorSerializer

class DeleteFactor(DestroyAPIView):
    queryset = Factor.objects.all()
    serializer_class = FactorSerializer

class FactorDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Factor.objects.all()
    serializer_class = FactorSerializer

class CalculatePriceView(APIView):
    def get(self, request):
        factors = Factor.objects.all()
        for item in factors:
            item.price = item.price - (item.price * item.cupon.percent / 100)
            item.save()
        return HttpResponse("Prices updated successfully")

class CreateFactorCustomView(APIView):
    def post(self, request):
        data = request.data
        cupon = Cupon.objects.get(id=data['cupon_id'])
        factor = Factor.objects.create(
            student_name=data['student_name'],
            price=data['price'],
            class1_id=data['class_id'],
            cupon=cupon,
            payment_status=data['payment_status']
        )
        factor.save()
        return HttpResponse("Factor created successfully")
