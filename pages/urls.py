from django.urls import path

from pages.views import ContactCreateView

app_name = 'pages'

urlpatterns = [
	path('contact/', ContactCreateView.as_view(), name='contact'),
]
