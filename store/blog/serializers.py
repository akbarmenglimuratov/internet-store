from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):

	class Meta:
		model = Blog
		exclude = ['text']

class BlogDetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Blog
		fields = '__all__'
