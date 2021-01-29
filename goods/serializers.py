from rest_framework import serializers
from goods.models import Goods

class CategoryGoodsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Goods
		fields = '__all__'