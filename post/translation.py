from modeltranslation.translator import register, TranslationOptions

from post.models import BlogModel, CategoryModel


@register(BlogModel)
class BlogTranslationOptions(TranslationOptions):
	fields = ('title', 'content', 'long_description', 'short_description',)


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
	fields = ('title',)
