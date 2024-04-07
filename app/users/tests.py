from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User


class AccountTests(APITestCase):

    def create_user(self):
        user = User.objects.create(
            email="testuser@gmail.com",
            name="Tester"
        )
        user.generate_referal_code()
        user.set_password("12345678")
        user.save()
        return user
    
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('registration')
        referer = self.create_user()
        data = {
            'email': 'seconduser@gmail.com',
            "password": "12345678",
            "name": "Tester",
            "referal_code": referer.my_referal_code
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        """
        Ensure we can create a new account object.
        """
        self.create_user()
        url = reverse('login')
        data = {
            'email': 'testuser@gmail.com',
            "password": "12345678",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_my_details(self):
        """
        Ensure we can create a new account object.
        """
        self.create_user()
        url = reverse('login')
        data = {
            'email': 'testuser@gmail.com',
            "password": "12345678",
        }
        login_response = self.client.post(url, data, format='json')
        token = login_response.json()["access"]
        url = reverse("my_details")
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION="Bearer "+token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_referals(self):
        """
        Ensure we can create a new account object.
        """
        referer = self.create_user()
        data = {
            'email': 'seconduser@gmail.com',
            "password": "12345678",
            "name": "Tester",
            "referal_code": referer.my_referal_code
        }
        url = reverse('registration')
        response = self.client.post(url, data, format='json')
        url = reverse('login')
        data = {
            'email': 'testuser@gmail.com',
            "password": "12345678",
        }
        response = self.client.post(url, data, format='json')
        token = response.json()["access"]
        url = reverse('my_referals')
        response = self.client.get(url, format='json', HTTP_AUTHORIZATION="Bearer "+token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
