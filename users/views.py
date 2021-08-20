from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView

from users.forms import ProfileModelForm
from users.models import ProfileModel


class ProfileUpdateView(UpdateView):
	model = ProfileModel
	form_class = ProfileModelForm
	template_name = 'profile.html'

	def get_object(self, queryset=None):
		profile, _ = ProfileModel.objects.get_or_create(user=self.request.user)
		return profile

	def get_success_url(self):
		return reverse('profile:home')
