from django.test import TestCase
from .models import Project
from user.models import User

class ProjectModelTest(TestCase):
    def setUp(self):
        self.u = User.objects.create(name='Taylor Swift', email='erastour@gmail.com')
        self.p = Project.objects.create(user_id=self.u, name='Eras Tour', description='Greatest concert on the planet', steps='Lights, camera, action!', colors='Black', features='Fire, Fireworks, slay', interactions='Get tickets, go to concert, scream', timeline='days', tagline='Best Concert Eva!!!', collaborators=2)

    def test_project_model_exists(self):
        projects = Project.objects.count()

        self.assertEqual(projects, 1)

    def test_project_model_has_attributes(self):
        self.assertEqual(self.p.user_id, self.u)
        self.assertEqual(self.p.name, 'Eras Tour')
        self.assertEqual(self.p.description, 'Greatest concert on the planet')
        self.assertEqual(self.p.steps, 'Lights, camera, action!')
        self.assertEqual(self.p.colors, 'Black')
        self.assertEqual(self.p.features, 'Fire, Fireworks, slay')
        self.assertEqual(self.p.interactions, 'Get tickets, go to concert, scream')

        self.assertEqual(self.p.timeline, 'days')
        self.assertEqual(self.p.tagline, 'Best Concert Eva!!!')
        self.assertEqual(self.p.collaborators, 2)

        self.assertEqual(self.p.saved, False)