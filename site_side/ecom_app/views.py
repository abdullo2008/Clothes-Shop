from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ProductModel, Category, UserModel
from .serializers import ProductSerializer, CategorySerializer, UserSerializer


# API Views
class CreateListProduct(ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class UpDelRetProduct(RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class CreateListCategory(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpDelRetCategory(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateListUser(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UpDelRetUser(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

# Site Views
