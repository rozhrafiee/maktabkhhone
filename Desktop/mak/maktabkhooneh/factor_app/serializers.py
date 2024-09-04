from rest_framework.serializers import ModelSerializer
from .models import Factor
from cupon_app.models import Cupon
from class_app.models import Clas

class CuponSerializer(ModelSerializer):
    class Meta:
        model = Cupon
        fields = "__all__"

class ClasSerializer(ModelSerializer):
    class Meta:
        model = Clas
        fields = "__all__"

class FactorSerializer(ModelSerializer):
    class Meta:
        model = Factor
        fields = "__all__"
