from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ContactModel(models.Model):
	name = models.CharField(max_length=255, verbose_name=_('name'))
	email = models.EmailField(null=True, verbose_name=_('email'))
	phone = models.CharField(max_length=25, verbose_name=_('phone'))
	message = models.TextField(null=True, verbose_name=_('message'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('contact')
		verbose_name_plural = _('contacts')
