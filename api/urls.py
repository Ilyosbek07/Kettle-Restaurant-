from django.urls import path

from api.views import CategoryListAPIView, FoodModelListAPIView, FoodRetrieveAPIView, BlogCategoryListAPIView, \
	BlogModelListAPIView, BlogRetrieveAPIView
from bot_users.views import OrderModelAPIView

app_name = 'api'

urlpatterns = [

	path('categories/', CategoryListAPIView.as_view()),
	path('categories/<int:pk>/', FoodModelListAPIView.as_view()),
	path('search/', FoodModelListAPIView.as_view()),
	path('cart_data/', FoodModelListAPIView.as_view()),
	path('orders/create/', OrderModelAPIView.as_view()),
	path('food/<int:pk>/', FoodRetrieveAPIView.as_view()),

	path('news_categories/', BlogCategoryListAPIView.as_view()),
	path('news_categories/<int:pk>/', BlogModelListAPIView.as_view()),
	path('news_search/', BlogModelListAPIView.as_view()),
	path('news/<int:pk>/', BlogRetrieveAPIView.as_view()),

]
