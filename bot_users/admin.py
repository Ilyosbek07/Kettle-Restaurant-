from django.contrib import admin

from bot_users.models import TelegramUserModel, OrderModel


@admin.register(TelegramUserModel)
class TelegramUserModelAdmin(admin.ModelAdmin):
	list_display = ['tg_id', 'username', 'first_name', 'last_name']
	list_filter = ['created_at']
	search_fields = ['username', 'first_name']


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
	list_display = ['price']
	list_filter = ['created_at']
	search_filter = ['user', 'product', 'price']
