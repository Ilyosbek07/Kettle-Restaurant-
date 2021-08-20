from django.db import models

from foods.models import ShopFoodsModel


class TelegramUserModel(models.Model):
	tg_id = models.IntegerField(unique=True)
	username = models.CharField(max_length=255, unique=True, null=True, blank=True)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.tg_id}({self.username}) | {self.first_name}'

	class Meta:
		verbose_name = 'Telegram user'
		verbose_name_plural = 'Telegram user'


class OrderModel(models.Model):
	user = models.ForeignKey(
		TelegramUserModel,
		related_name='orders',
		on_delete=models.CASCADE
	)
	product = models.ManyToManyField(
		ShopFoodsModel,
		related_name='orders'
	)
	price = models.FloatField()

	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user)

	class Meta:
		verbose_name = 'order'
		verbose_name_plural = 'orders'
