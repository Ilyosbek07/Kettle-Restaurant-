from django.urls import path

from bot_users.views import TelegramRegisterCreateAPIView, OrderHistoryListAPIView

app_name = 'tg_users'

urlpatterns = [
	path('register/', TelegramRegisterCreateAPIView.as_view()),
	path('history/', OrderHistoryListAPIView.as_view()),
]
