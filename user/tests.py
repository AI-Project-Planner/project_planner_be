from django.test import TestCase, Client
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        self.u = User.objects.create(name='Taylor Swift', email='erastour@gmail.com')
        global c
        c = Client()

    def test_user_model_exists(self):
        users = User.objects.count()

        self.assertEqual(users, 1)

    def test_user_model_has_attributes(self):
        self.assertEqual(self.u.name, 'Taylor Swift')
        self.assertEqual(self.u.email, 'erastour@gmail.com')

    def test_find_or_create_user(self):
        payload = {
            "name": "michael c",
            "email": "myemail@gmail.com"
        }
        response = c.post(f"/api/v1/users/", data=payload, content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_find_or_create_user_but_user_already_exists(self):
        payload = {
            "name": "michael c",
            "email": "myemail@gmail.com"
        }
        response = c.post(f"/api/v1/users/", data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = c.post(f"/api/v1/users/", data=payload, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'data')
        self.assertContains(response, 'id')
        self.assertContains(response, 'type')
        self.assertContains(response, 'attributes')
        self.assertContains(response, 'name')
        self.assertContains(response, 'email')