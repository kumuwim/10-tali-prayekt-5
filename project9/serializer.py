from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSerializers(ModelSerializer):
    class Meta:
        model=Product
        fields=["id","name","created_at","price","discriptions"]
        read_only_fields=["id"]
