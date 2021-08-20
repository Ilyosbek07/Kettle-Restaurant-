from django import template
from django.db.models import Sum

from foods.models import ShopFoodsModel
from foods.utils import get_cart_lengs

register = template.Library()


@register.simple_tag
def get_lang_url(request, lang):
	url = request.path.split('/')
	url[1] = lang
	return '/'.join(url)


@register.filter
def in_cart(object, request):
	return object.pk in request.session.get('cart', [])


@register.simple_tag
def count_cart(request):
	return get_cart_lengs(request)


@register.simple_tag
def cart_price(request):
	if get_cart_lengs(request) == 0:
		return 0

	return ShopFoodsModel.get_from_cart(request).aggregate(
		Sum('price')
	).get('price__sum', 0)
