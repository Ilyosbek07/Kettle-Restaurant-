from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import FoodCategoryModelSerializer, FoodModelSerializer, BlogCategoryModelSerializer, \
	BlogModelSerializer
from foods.models import ShopFoodsModel, FoodCategoryModel
from post.models import CategoryModel, BlogModel


class CategoryListAPIView(ListAPIView):
	serializer_class = FoodCategoryModelSerializer
	queryset = FoodCategoryModel.objects.all()


class FoodModelListAPIView(ListAPIView):
	serializer_class = FoodModelSerializer

	def get_queryset(self):
		pk = self.kwargs.get('pk')
		q = self.request.GET.get('q')
		cart = self.request.GET.get('products')

		if pk:
			return ShopFoodsModel.objects.filter(category_id=pk)
		elif q:
			return ShopFoodsModel.objects.filter(title__icontains=q)
		elif cart:
			cart = cart.strip('[]').replace('\'', '').split(',')
			return ShopFoodsModel.objects.filter(pk__in=cart)
		else:
			return ShopFoodsModel.objects.none()


class FoodRetrieveAPIView(RetrieveAPIView):
	serializer_class = FoodModelSerializer
	queryset = ShopFoodsModel.objects.all()


class BlogCategoryListAPIView(ListAPIView):
	serializer_class = BlogCategoryModelSerializer
	queryset = CategoryModel.objects.all()


class BlogModelListAPIView(ListAPIView):
	serializer_class = BlogModelSerializer

	def get_queryset(self):
		pk = self.kwargs.get('pk')
		b = self.request.GET.get('b')

		if pk:
			return BlogModel.objects.filter(category_id=pk)
		elif b:
			return BlogModel.objects.filter(title__icontains=b)
		else:
			return BlogModel.objects.none()


class BlogRetrieveAPIView(RetrieveAPIView):
	serializer_class = BlogModelSerializer
	queryset = BlogModel.objects.all()
