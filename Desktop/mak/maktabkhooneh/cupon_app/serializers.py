from rest_framework.serializers import ModelSerializer
from .models import Cupon

class CuponSerializer(ModelSerializer):
    class Meta:
        model = Cupon
        fields = "__all__"
