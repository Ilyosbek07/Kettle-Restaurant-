from rest_framework import serializers

from foods.models import FoodCategoryModel, ShopFoodsModel
from post.models import CategoryModel, BlogModel


class FoodCategoryModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = FoodCategoryModel
		fields = '__all__'


class FoodModelSerializer(serializers.ModelSerializer):
	category = FoodCategoryModelSerializer()

	class Meta:
		model = ShopFoodsModel
		fields = '__all__'


class BlogCategoryModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategoryModel
		fields = ['title']


class BlogModelSerializer(serializers.ModelSerializer):
	category = BlogCategoryModelSerializer()

	class Meta:
		model = BlogModel
		fields = ['title']
