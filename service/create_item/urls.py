from django.urls import path

from create_item import views

app_name = 'item'

urlpatterns = [
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]