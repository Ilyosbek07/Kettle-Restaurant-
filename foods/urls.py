from django.urls import path

from foods.views import CartListView, \
	HomeTemplateView, ShopListView, \
	AboutHomeTemplate, ShopDetailView, add_to_cart, CommentCreateView

app_name = 'foods'

urlpatterns = [
	# path('checkout/', CheckoutTemplateView.as_view(), name='checkout'),
	path('menu/', ShopListView.as_view(), name='shop'),
	path('detail/<int:pk>/', ShopDetailView.as_view(), name='detail'),
	path('card/', CartListView.as_view(), name='card'),
	path('', HomeTemplateView.as_view(), name='home'),
	path('cart/<int:pk>/', add_to_cart, name='add_to_cart'),
	path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
	path('about/', AboutHomeTemplate.as_view(), name='about'),
]
