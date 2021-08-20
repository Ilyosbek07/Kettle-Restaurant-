from django.urls import path

from order.views import OrderCreateView

app_name = 'order'

urlpatterns = [
	path('', OrderCreateView.as_view(), name='home')
]
