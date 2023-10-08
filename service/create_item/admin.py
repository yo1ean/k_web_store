from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from create_item.models import Item

admin.site.register(Item)

