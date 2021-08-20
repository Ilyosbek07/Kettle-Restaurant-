from django.urls import path

from post.views import BlogListView, BlogDetailView, CommentCreateView

app_name = 'post'

urlpatterns = [
	path('', BlogListView.as_view(), name='blog'),
	path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
	path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
]
