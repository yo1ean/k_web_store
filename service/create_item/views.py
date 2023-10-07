from django.shortcuts import render, redirect

from create_item.forms import ItemForm
from create_item.models import Item


def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ItemForm()
    return render(request, 'item.html', {'form': form})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})