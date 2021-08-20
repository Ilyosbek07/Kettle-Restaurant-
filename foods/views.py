from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from foods.forms import Comment2ModelForm
from foods.models import AboutModel, HomeFoodModel, ImageModel, ShopFoodsModel, FoodTagModel, FoodCategoryModel, \
	ChefsModel
from post.models import BlogModel


class HomeTemplateView(ListView):
	template_name = 'index.html'
	queryset = HomeFoodModel.objects.order_by('-pk')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['about'] = AboutModel.objects.all()
		context['images'] = ImageModel.objects.order_by('pk')
		context['tags'] = FoodTagModel.objects.order_by('pk')
		context['newss'] = BlogModel.objects.order_by('pk')[:4]

		return context


class AboutHomeTemplate(TemplateView):
	template_name = 'about-us.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['about'] = AboutModel.objects.order_by('-pk')
		context['chefs'] = ChefsModel.objects.order_by('pk')

		return context


# def get_context_data(self, **kwargs):
# 	context = super().get_context_data(**kwargs)
#
# 	context['story'] = AboutHomeModel.objects.order_by('-pk')
#
# 	return context


class ShopListView(ListView):
	template_name = 'shop.html'
	paginate_by = 6

	def get_queryset(self):
		qs = ShopFoodsModel.objects.order_by('-pk')
		q = self.request.GET.get('q')
		sort = self.request.GET.get('sort')

		if q:
			qs = qs.filter(title__icontains=q)

		if sort:
			if sort == 'price':
				qs = sorted(qs, key=lambda i: i.get_price())
			elif sort == '-price':
				qs = sorted(qs, key=lambda i: i.get_price(), reverse=True)

		return qs


class ShopDetailView(DetailView):
	template_name = 'shop-single.html'
	model = ShopFoodsModel


# class CheckoutTemplateView(TemplateView):
# 	template_name = 'checkout.html'


class CartListView(ListView):
	template_name = 'shopping-cart.html'

	def get_queryset(self):
		return ShopFoodsModel.get_from_cart(self.request)


class CommentCreateView(CreateView):
	form_class = Comment2ModelForm

	def form_valid(self, form):
		form.instance.blog = get_object_or_404(ShopFoodsModel, pk=self.kwargs.get('pk'))
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('foods:detail', kwargs={'pk': self.kwargs.get('pk')})


def add_to_cart(request, pk):
	cart = request.session.get('cart', [])

	if pk in cart:
		cart.remove(pk)
	else:
		cart.append(pk)

	request.session['cart'] = cart

	return redirect(request.GET.get('next', '/'))
