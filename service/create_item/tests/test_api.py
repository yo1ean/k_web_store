from django.urls import reverse
from rest_framework.test import APITestCase

class ItemsApiCase(APITestCase):
    def test_get(self):
        url = reverse('item_list')
        print(url)
        responce = self.client.get(url)
        print(responce.data)