from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LogoutView
from django.urls import path

from create_item import views
from create_item.views import is_admin

urlpatterns = [
    path('df-admin/', admin.site.urls),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('admin/', user_passes_test(is_admin)(views.admin_panel), name='admin_panel'),
    path('add_item/', views.create_item, name='add_item'),
    path('item_list/', views.item_list, name='item_list'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('item/<str:item_name>/', views.item_detail, name='item_detail'),
    path('item/<str:item_name>/update/', views.item_update, name='item_update'),
    path('item/<str:item_name>/delete/', views.item_delete, name='item_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
