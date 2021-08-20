from rest_framework import serializers

from bot_users.models import TelegramUserModel, OrderModel


class TelegramUsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = TelegramUserModel
		fields = '__all__'


class HistoryModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderModel
		exclude = ['created_at', 'user']
