from django.test import TestCase, Client
from project.models import Project
from user.models import User
import json, code

class GetProjectCase(TestCase):
    def setUp(self):
        global u
        u = User.objects.create(name='Taylor Swift', email='erastour@gmail.com')
        global p
        p = Project.objects.create(user=u, name='Eras Tour', description='Greatest concert on the planet', steps='Lights, camera, action!', colors='Black', features='Fire, Fireworks, slay', interactions='Get tickets, go to concert, scream', timeline='7 days')
        global c
        c = Client()

    def test_project_is_returned(self):
        response = c.get(f"/api/v1/projects/{p.id}/")
        self.assertEqual(response.status_code, 200)

        returned_project = json.loads(response.content)["data"]

        self.assertEqual(returned_project["id"], f"{p.id}")
        self.assertEqual(returned_project["type"], "project")
        self.assertEqual(returned_project["attributes"]["user"], p.user.id)
        self.assertEqual(returned_project["attributes"]["name"], p.name)
        self.assertEqual(returned_project["attributes"]["description"], p.description)
        self.assertEqual(returned_project["attributes"]["steps"], p.steps)
        self.assertEqual(returned_project["attributes"]["colors"], p.colors)
        self.assertEqual(returned_project["attributes"]["features"], p.features)
        self.assertEqual(returned_project["attributes"]["interactions"], p.interactions)
        self.assertEqual(returned_project["attributes"]["timeline"], p.timeline)
        self.assertEqual(returned_project["attributes"]["saved"], p.saved)