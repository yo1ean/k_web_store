from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy

from create_item.forms import ProductForm


def is_admin(user):
    return user.groups.filter(name='admins').exists()


@user_passes_test(is_admin)
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = ProductForm()
    return render(request, 'admin/add_product.html', {'form': form})


@user_passes_test(is_admin)
def admin_panel(request):
    return render(request, 'admin/admin_panel.html')


class CustomLoginView(LoginView):
    template_name = 'admin/login.html'

    def get_success_url(self):
        return reverse_lazy('admin_panel')
