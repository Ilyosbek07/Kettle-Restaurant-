from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from foods.models import ShopFoodsModel


class CategoryModel(models.Model):
	title = models.CharField(max_length=25, verbose_name=_('name'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('category')
		verbose_name_plural = _('categories')


class BlogTagModel(models.Model):
	title = models.CharField(max_length=25, verbose_name=_('title'))

	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('blog tag')
		verbose_name_plural = _('blog tags')


class BlogModel(models.Model):
	title = models.CharField(max_length=55, verbose_name=_('title'))
	content = RichTextUploadingField(verbose_name=_('content'))
	image = models.ImageField(null=True, verbose_name=_('image'))
	short_description = RichTextUploadingField(verbose_name=_('short descriptions'))
	long_description = RichTextUploadingField(verbose_name=_('long descriptions'))
	tags = models.ManyToManyField(
		BlogTagModel,
		related_name='tag'
	)
	category = models.ManyToManyField(
		CategoryModel,
		related_name='category'
	)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

	def get_comments(self):
		return self.comments.order_by('-created_at')

	def get_prev2(self):
		return self.get_previous_by_created_at()

	def get_next2(self):
		return self.get_next_by_created_at()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('blog')
		verbose_name_plural = _('blogs')


class CommentModel(models.Model):
	blog = models.ForeignKey(
		BlogModel,
		on_delete=models.CASCADE,
		related_name='comments'
	)
	# shop = models.ForeignKey(
	# 	ShopFoodsModel,
	# 	on_delete=models.CASCADE,
	# 	related_name='comments2'
	# )
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
