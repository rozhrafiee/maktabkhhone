from rest_framework.serializers import ModelSerializer
from .models import Clas
from category_app.models import Category
from category_app.serializers import CategorySerializer

class ClasSerializer(ModelSerializer):
    category = CategorySerializer()  # Nested serializer to include category info

    class Meta:
        model = Clas
        fields = "__all__"
