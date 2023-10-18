from django.contrib.auth.decorators import user_passes_test
from django.urls import path

from custom_admin_panel import views
from custom_admin_panel.views import is_admin

urlpatterns = [
    path('', user_passes_test(is_admin)(views.admin_panel), name='admin_panel'),
    path('add_item/', views.create_product, name='add_item'),
]