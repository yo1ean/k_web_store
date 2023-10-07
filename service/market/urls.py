from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from create_item import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', views.create_item, name='item'),
    path('item_list/', views.item_list, name='item_list')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
