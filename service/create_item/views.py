from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from create_item.models import Product


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})

