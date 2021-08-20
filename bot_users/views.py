from django.db.models import Sum
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from bot_users.models import TelegramUserModel, OrderModel
from bot_users.serializers import TelegramUsersSerializer, HistoryModelSerializer
from foods.models import ShopFoodsModel


class TelegramRegisterCreateAPIView(CreateAPIView):
	serializer_class = TelegramUsersSerializer
	queryset = TelegramUserModel.objects.all()


class OrderModelAPIView(APIView):
	def post(self, request, *args, **kwargs):
		user_id = request.POST.get('user_id')
		user = TelegramUserModel.objects.get(tg_id=user_id)

		products = request.POST.get('products')
		products = products.strip('[]').replace('\'', '').split(',')

		products = ShopFoodsModel.objects.filter(pk__in=products)
		price = products.aggregate(Sum('price'))['price__sum']

		order = OrderModel.objects.create(
			user=user,
			price=price
		)

		order.products.set(products)
		order.save()

		return Response(data={'status': 'ok'})


class OrderHistoryListAPIView(ListAPIView):
	serializer_class = HistoryModelSerializer
	queryset = OrderModel.objects.all()
