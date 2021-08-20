from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from post.forms import CommentModelForm
from post.models import BlogModel, CategoryModel, BlogTagModel, CommentModel


class BlogListView(ListView):
	template_name = 'blog-list.html'
	paginate_by = 3

	def get_queryset(self):
		qs = BlogModel.objects.order_by('pk')
		s = self.request.GET.get('s')
		cat = self.request.GET.get('cat')
		tag = self.request.GET.get('tag')

		if s:
			qs = qs.filter(title__icontains=s)
			print(qs)
		if cat:
			qs = qs.filter(category__id=cat)
		if tag:
			qs = qs.filter(category__id=tag)

		return qs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['tags'] = BlogTagModel.objects.all()
		context['categories'] = CategoryModel.objects.all()

		return context


class BlogDetailView(DetailView):
	template_name = 'blog-details.html'
	model = BlogModel


class CommentCreateView(CreateView):
	form_class = CommentModelForm

	def form_valid(self, form):
		form.instance.blog = get_object_or_404(BlogModel, pk=self.kwargs.get('pk'))
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('post:detail', kwargs={'pk': self.kwargs.get('pk')})
