from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from post.models import BlogModel, CommentModel, CategoryModel, BlogTagModel


class MyTranslationAdmin1(TranslationAdmin):
	class Media:
		js = (
			'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
			'modeltranslation/js/tabbed_translation_fields.js',
		)
		css = {
			'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
		}


@admin.register(BlogModel)
class BlogModelAdmin(MyTranslationAdmin1):
	list_display = ['title', 'content']
	list_filter = ['created_at']
	search_fields = ['title']
	autocomplete_fields = ['tags', 'category']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'message']
	list_filter = ['created_at']
	search_fields = ['first_name', 'email']


@admin.register(BlogTagModel)
class CommentModelAdmin(admin.ModelAdmin):
	list_display = ['title']
	list_filter = ['created_at']
	search_fields = ['title']


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin1):
	list_display = ['title']
	list_filter = ['created_at']
	search_fields = ['title']
