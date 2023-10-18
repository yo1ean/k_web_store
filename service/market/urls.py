from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from custom_admin_panel import views

urlpatterns = [
    path('df-admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('admin/', include('custom_admin_panel.urls')),
    path('item/', include('create_item.urls')),
    path('', include('homepage.urls')),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
