from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from foods.models import HomeFoodModel

UserModel = get_user_model()


class OrderModel(models.Model):
	user = models.ForeignKey(UserModel, related_name='order', on_delete=models.CASCADE)
	food = models.ManyToManyField(HomeFoodModel, related_name='order')
	first_name = models.CharField(max_length=55, verbose_name=_('first name'))
	last_name = models.CharField(max_length=55, verbose_name=_('last name'))
	company = models.CharField(max_length=55, verbose_name=_('company'))
	phone = models.IntegerField(null=True, verbose_name=_('phone'))
	email = models.EmailField(null=True, verbose_name=_('email'))
	address1 = models.CharField(max_length=55, verbose_name=_('address1'))
	address2 = models.CharField(max_length=55, verbose_name=_('address2'))
	city = models.CharField(max_length=55, verbose_name=_('city'))
	state = models.CharField(max_length=55, verbose_name=_('state'))
	postcode = models.CharField(max_length=55, verbose_name=_('postcode'))

	created_at = models.DateTimeField(auto_now=True, verbose_name=_('created_at'))

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	class Meta:
		verbose_name = _('order')
		verbose_name_plural = _('orders')
