def get_cart_lengs(request):
	return len(request.session.get('cart', []))
