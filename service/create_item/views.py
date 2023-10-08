from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404

from create_item.forms import ItemForm
from create_item.models import Item


def is_admin(user):
    return user.groups.filter(name='admins').exists()


@user_passes_test(is_admin)
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})


@user_passes_test(is_admin)
def admin_panel(request):
    # Ваш код для административной панели
    return render(request, 'admin_panel.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'


def item_detail(request, item_name):
    item = get_object_or_404(Item, name=item_name)
    return render(request, 'item_detail.html', {'item': item})


@user_passes_test(is_admin)
def item_update(request, item_name):
    item = get_object_or_404(Item, name=item_name)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)

    return render(request, 'item_update.html', {'form': form, 'item': item, 'update_mode': True})


@user_passes_test(is_admin)
def item_delete(request, item_name):
    item = get_object_or_404(Item, name=item_name)

    if request.method == 'POST':
        item.delete()
        return redirect('item_list')

    return render(request, 'item_delete.html', {'item': item})