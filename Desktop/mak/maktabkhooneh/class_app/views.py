from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Clas
from .serializers import ClasSerializer
from django.http import HttpResponse

class ClasList(ListAPIView):
    queryset = Clas.objects.all()
    serializer_class = ClasSerializer

class ClasDetail(RetrieveAPIView):
    queryset = Clas.objects.all()
    serializer_class = ClasSerializer

class CreateClas(CreateAPIView):
    queryset = Clas.objects.all()
    serializer_class = ClasSerializer

class UpdateClas(UpdateAPIView):
    queryset = Clas.objects.all()
    serializer_class = ClasSerializer

class DeleteClas(DestroyAPIView):
    queryset = Clas.objects.all()
    serializer_class = ClasSerializer

class ClasDetailUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Clas.objects.all()
    serializer_class = ClasSerializer
