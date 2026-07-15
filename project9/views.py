from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializer import ProductSerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

# Create your views here.