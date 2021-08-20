from datetime import datetime

import pytz
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class FoodCategoryModel(models.Model):
	title = models.CharField(max_length=255, verbose_name=_('title'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('food category')
		verbose_name_plural = _('food categories')


class FoodTagModel(models.Model):
	title = models.CharField(max_length=255, verbose_name=_('name'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('food tag')
		verbose_name_plural = _('food tags')


class ShopFoodsModel(models.Model):
	title = models.CharField(max_length=25, verbose_name=_('title'))
	content = models.TextField(null=True, verbose_name=_('content'))
	description = RichTextUploadingField(verbose_name=_('description'))
	price = models.FloatField(verbose_name=_('price'))
	image = models.ImageField(null=True, verbose_name=_('image'))
	category = models.ForeignKey(
		FoodCategoryModel,
		related_name='foods',
		on_delete=models.PROTECT,
		null=True, blank=True
	)

	def get_comments2(self):
		return self.comments2.order_by('-created_at')

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	def get_related_products2(self):
		return self.category.foods.exclude(pk=self.pk)

	def get_price(self):
		return self.price

	@staticmethod
	def get_from_cart(request):
		cart = request.session.get('cart', [])
		return ShopFoodsModel.objects.filter(
			pk__in=cart
		)

	def is_new(self):
		time = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
		return time.days <= 3

	class Meta:
		verbose_name = _('shop food')
		verbose_name_plural = _('shop foods')


class HomeFoodModel(models.Model):
	price = models.FloatField(verbose_name=_('price'))
	food_name = models.CharField(max_length=25, verbose_name=_('food name'))
	image = models.ImageField(null=True, verbose_name=_('image'))
	tags = models.ManyToManyField(
		FoodTagModel,
		related_name='pages',
	)
	category = models.ManyToManyField(
		FoodCategoryModel,
		related_name='category',
	)
	# structure = models.ForeignKey()

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def get_prev(self):
		return self.get_previous_by_created_at()

	def get_next(self):
		return self.get_next_by_created_at()

	def __str__(self):
		return f'{self.food_name} {self.tags}'

	class Meta:
		verbose_name = _('home food')
		verbose_name_plural = _('home foods')


#

class ChefsModel(models.Model):
	description = RichTextUploadingField(verbose_name=_('description'))
	name = models.CharField(max_length=255, verbose_name=_('name'))
	image = models.ImageField(null=True, verbose_name=_('image'))
	job = models.CharField(max_length=255, verbose_name=_('job'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('chef')
		verbose_name_plural = _('chefs')


class AboutModel(models.Model):
	title = models.CharField(max_length=255, verbose_name=_('title'))
	content = models.TextField(verbose_name=_('content'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('About')


class ImageModel(models.Model):
	title = models.CharField(max_length=255, verbose_name=_('title'))
	image = models.ImageField(null=True, verbose_name=_('image'))
	tags = models.ManyToManyField(
		FoodTagModel,
		related_name='image',
	)

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	class Meta:
		verbose_name = _('image')
		verbose_name_plural = _('images')


class Comment2Model(models.Model):
	shop = models.ForeignKey(
		ShopFoodsModel,
		on_delete=models.CASCADE,
		related_name='comments2'
	)
	first_name = models.CharField(max_length=255, verbose_name=_('first name'))
	email = models.EmailField(null=True, verbose_name=_('email'))
	message = models.TextField(null=True, verbose_name=_('message'))
	image = models.ImageField(null=True)

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.first_name

	class Meta:
		verbose_name = _('comment')
		verbose_name_plural = _('comment')
