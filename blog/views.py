from django.shortcuts import render
from rest_framework import generics
from blog.serializers import *
from blog.models import Blog

class BlogListView(generics.ListAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogDetailSerializer
	lookup_field = "slug"