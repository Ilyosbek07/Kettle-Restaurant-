from modeltranslation.translator import register, TranslationOptions

from foods.models import ChefsModel, AboutModel, FoodTagModel, HomeFoodModel, FoodCategoryModel, ImageModel, ShopFoodsModel


@register(ChefsModel)
class ChefTranslationOptions(TranslationOptions):
	fields = ('description',)


@register(AboutModel)
class AboutTranslationOptions(TranslationOptions):
	fields = ('title', 'content',)


@register(FoodTagModel)
class FoodTagTranslationOptions(TranslationOptions):
	fields = ('title',)


@register(HomeFoodModel)
class HomeFoodTranslationOptions(TranslationOptions):
	fields = ('food_name',)


@register(FoodCategoryModel)
class FoodCategoryTranslationOptions(TranslationOptions):
	fields = ('title',)


@register(ImageModel)
class ImageTranslationOptions(TranslationOptions):
	fields = ('title',)


@register(ShopFoodsModel)
class ShopFoodsTranslationOptions(TranslationOptions):
	fields = ('title', 'content', 'description',)
