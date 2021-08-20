from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from foods.models import HomeFoodModel
from order.models import OrderModel
# from pages.models import FoodModel


class OrderCreateView(CreateView):
	form_class = OrderModel
	template_name = 'checkout.html'
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['foods'] = HomeFoodModel.objects.get_from_cart(self.request)
		context['profile'] = self.request.user.profile

		return context
