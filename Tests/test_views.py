from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        # Create some Menu instances
        self.menu1 = Menu.objects.create(title="Pizza", price=12.50, inventory=20)
        self.menu2 = Menu.objects.create(title="Burger", price=9.99, inventory=15)
        self.menu3 = Menu.objects.create(title="Pasta", price=14.00, inventory=10)

    def test_getall(self):
        # Get all Menu objects
        response = self.client.get(reverse('menu-list'))  # Assuming router name is 'menu-list'

        # Serialize the test data
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many=True)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
