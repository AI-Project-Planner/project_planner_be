from django.test import TestCase, Client
from .models import Project
from user.models import User
import json, code

class ProjectModelTest(TestCase):
    def setUp(self):
        self.u = User.objects.create(name='Taylor Swift', email='erastour@gmail.com')
        self.p = Project.objects.create(user_id=self.u, name='Eras Tour', description='Greatest concert on the planet', steps='Lights, camera, action!', colors='Black', features='Fire, Fireworks, slay', interactions='Get tickets, go to concert, scream', timeline='days', tagline='Best Concert Eva!!!', collaborators=2)
        global c
        c = Client()

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

    def test_project_is_returned(self):
        response = c.get(f"/api/v1/projects/{p.id}/")
        self.assertEqual(response.status_code, 200)

        returned_project = json.loads(response.content)["data"]

        payload = {
        "model": "gpt-3.5-turbo-16k",
        "messages": [
                {
                "role": "user",
                "content": "Create a plan for a full stack application using react, typescript, and express. I have 60 days to build this application. Include additional feature ideas that the application could have. There will be 8 people working on this project.",
                "role": "system",
                "content": "In this plan, please include a name for the application, a schedule for project completion, a plan for how the users would interact with the application, and provide an example interaction. Include a color palette with 6 colors for this app. Provide your new response in JSON format with the following Keys: ProjectName, Description, Steps, Features, Interactions, ColorPalette, and Tagline. Tagline should be a five word summary of the project description. Steps, Features, Interaction and ColorPalette values should come back as an array. Any value inside of an array should not be numbered."
                }
            ]
        }
