from django.test import TestCase
from .models import User

class UserModelTest(TestCase):
    def setUp(self):
        self.u = User.objects.create(name='Taylor Swift', email='erastour@gmail.com')

    def test_user_model_exists(self):
        users = User.objects.count()

        self.assertEqual(users, 1)

    def test_user_model_has_attributes(self):
        self.assertEqual(self.u.name, 'Taylor Swift')
        self.assertEqual(self.u.email, 'erastour@gmail.com')

