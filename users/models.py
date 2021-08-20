from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class ProfileModel(models.Model):
	user = models.OneToOneField(UserModel, related_name='profile', on_delete=models.CASCADE)
	first_name = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('first name'))
	last_name = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('last name'))
	phone = models.IntegerField(null=True, blank=True, verbose_name=_('phone'))
	email = models.EmailField(null=True, blank=True, verbose_name=_('email'))
	company = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('company'))
	country = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('country'))
	address1 = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('address1'))
	address2 = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('address2'))
	city = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('city'))
	state = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('state'))
	postcode = models.CharField(max_length=55, null=True, blank=True, verbose_name=_('post code'))

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	class Meta:
		verbose_name = _('profile')
		verbose_name_plural = _('profiles')
