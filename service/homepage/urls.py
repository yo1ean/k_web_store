from django.urls import path

from homepage import views
from homepage.views import HomeView

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_list/<slug:category_slug>/', views.product_list, name='products_category')
]

