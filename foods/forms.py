from django import forms

from foods.models import Comment2Model


class Comment2ModelForm(forms.ModelForm):
	class Meta:
		model = Comment2Model
		exclude = ['email', 'shop', 'image']
