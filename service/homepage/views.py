from django.shortcuts import render, get_object_or_404
from django.views import View

from create_item.models import Product, Category


class HomeView(View):
    def get(self, request):
        return render(request, 'shop/homepage/home.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })
