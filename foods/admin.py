from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from foods.models import ChefsModel, AboutModel, HomeFoodModel, FoodTagModel, ImageModel, FoodCategoryModel, \
	ShopFoodsModel


class MyTranslationAdmin2(TranslationAdmin):
	class Media:
		js = (
			'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
			'modeltranslation/js/tabbed_translation_fields.js',
		)
		css = {
			'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
		}


@admin.register(HomeFoodModel)
class FoodModelAdmin(MyTranslationAdmin2):
	list_display = ['food_name', 'price']
	list_filter = ['created_at']
	search_fields = ['food_name']
	autocomplete_fields = ['tags', 'category']


@admin.register(FoodTagModel)
class FoodTagModelAdmin(MyTranslationAdmin2):
	list_display = ['title']
	list_filter = ['created_at']
	search_fields = ['title']


@admin.register(FoodCategoryModel)
class FoodCategoryAdmin(MyTranslationAdmin2):
	list_display = ['title']
	list_filter = ['created_at']
	search_fields = ['title']


@admin.register(ImageModel)
class ImageModelAdmin(MyTranslationAdmin2):
	list_display = ['title']
	list_filter = ['created_at']
	search_fields = ['title']


@admin.register(ShopFoodsModel)
class ShopFoodsModelAdmin(MyTranslationAdmin2):
	list_display = ['title', 'content']
	list_filter = ['created_at']
	search_fields = ['title', 'content']
	# autocomplete_fields = ['category']


@admin.register(ChefsModel)
class ChefsModelAdmin(MyTranslationAdmin2):
	list_display = ['name']
	list_filter = ['created_at']
	search_fields = ['name']


@admin.register(AboutModel)
class AboutModelAdmin(MyTranslationAdmin2):
	list_display = ['content', 'title']
	list_filter = ['created_at']
	search_fields = ['title', 'content']
