from django.shortcuts import render
from .serializers import CategorySerializer
from .models import Category
from rest_framework.response import Response
from rest_framework import viewsets



class CategoryViewSet(viewsets.ModelViewSet):

    queryset=Category.objects.all().order_by("-created")
    serializer_class=CategorySerializer

    
