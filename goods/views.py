from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from goods.models import Goods
from goods.serializers import *

class CategoryViews(generics.ListAPIView):
	queryset = Goods.objects.all()
	serializer_class = CategoryGoodsSerializer
