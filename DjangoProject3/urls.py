from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
	path('accounts/', include('registration.backends.default.urls')),
	path('admin/', admin.site.urls),
	path('', include('foods.urls', namespace='foods')),
	path('profile/', include('users.urls', namespace='profile')),
	path('order/', include('order.urls', namespace='order')),
	path('post/', include('post.urls', namespace='post')),
	path('pages/', include('pages.urls', namespace='pages')),
	path('api/', include('api.urls', namespace='api')),
	path('tg_users/', include('bot_users.urls', namespace='tg_users')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
