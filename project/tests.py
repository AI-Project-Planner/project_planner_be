from django.test import TestCase, Client
from .models import Project
from user.models import User

class ProjectModelTest(TestCase):
    def setUp(self):
        self.u = User.objects.create(name='Taylor Swift', email='erastour@gmail.com')
        self.p = Project.objects.create(user_id=self.u, name='Eras Tour', description='Greatest concert on the planet', steps='Lights, camera, action!', colors='Black', features='Fire, Fireworks, slay', technologies='react, typescript and javascript', interactions='Get tickets, go to concert, scream', timeline='days', timeline_int=1, tagline='Best Concert Eva!!!', collaborators=2)
        self.q = Project.objects.create(user_id=self.u, saved=True, name='Eras Tour', description='Greatest concert on the planet', steps='Lights, camera, action!', colors='Black', features='Fire, Fireworks, slay', technologies='react, typescript and javascript', interactions='Get tickets, go to concert, scream', timeline='days', timeline_int=5, tagline='Best Concert Eva!!!', collaborators=2)
        global c
        c = Client()

    def test_project_model_exists(self):
        projects = Project.objects.count()

        self.assertEqual(projects, 2)

    def test_project_model_has_attributes(self):
        self.assertEqual(self.p.user_id, self.u)
        self.assertEqual(self.p.name, 'Eras Tour')
        self.assertEqual(self.p.description, 'Greatest concert on the planet')
        self.assertEqual(self.p.steps, 'Lights, camera, action!')
        self.assertEqual(self.p.colors, 'Black')
        self.assertEqual(self.p.features, 'Fire, Fireworks, slay')
        self.assertEqual(self.p.technologies, 'react, typescript and javascript')
        self.assertEqual(self.p.interactions, 'Get tickets, go to concert, scream')
        self.assertEqual(self.p.timeline, 'days')
        self.assertEqual(self.p.timeline_int, 1)
        self.assertEqual(self.p.tagline, 'Best Concert Eva!!!')
        self.assertEqual(self.p.collaborators, 2)
        self.assertEqual(self.p.saved, False)

    def test_project_is_returned(self):
        payload = {
            "type": "frontend",
            "technologies": "react, typescript and javascript",
            "time": "1 week",
            "collaborators": 2
        }

        response = c.post(f"/api/v1/users/{self.u.id}/projects/", data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'data')
        self.assertContains(response, 'id')
        self.assertContains(response, 'type')
        self.assertContains(response, 'attributes')
        self.assertContains(response, 'user_id')
        self.assertContains(response, 'name')
        self.assertContains(response, 'technologies')
        self.assertContains(response, 'description')
        self.assertContains(response, 'features')
        self.assertContains(response, 'interactions')
        self.assertContains(response, 'colors')
        self.assertContains(response, 'saved')
        self.assertContains(response, 'tagline')
        self.assertContains(response, 'timeline')
        self.assertContains(response, 'timeline_int')

    def test_project_is_not_returned(self):
        payload = {
            "type": "frontend",
            "technologies": "react, typescript and javascript",
            "time": "1 week",
            "collaborators": 2
        }

        response = c.post("/api/v1/users/-1/projects/", data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_project_is_updated(self):
        payload = {
            "saved": "true"
        }

        response = c.patch(f"/api/v1/users/{self.u.id}/projects/{self.p.id}/", data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 202)

    def test_project_cant_be_updated_user_id(self):
        payload = {
            "saved": "true"
        }

        response = c.patch(f"/api/v1/users/-1/projects/{self.p.id}/", data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_project_cant_be_updated_project_id(self):
        payload = {
            "saved": "true"
        }

        response = c.patch(f"/api/v1/users/{self.u.id}/projects/-1/", data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_project_cant_be_generated(self):
        payload = {
            "type": "frontend",
            "technologies": "react, typescript and javascript",
            "time": "1 week",
            "collaborators": 2
        }

        response = c.post("/api/v1/users/-1/projects/", data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_get_all_users_projects(self):
        response = c.get(f"/api/v1/users/{self.u.id}/projects/")
        self.assertEqual(response.status_code, 200)

    def test_get_all_users_projects_user_not_found(self):
        response = c.get("/api/v1/users/-1/projects/")
        self.assertEqual(response.status_code, 404)

    def test_project_deletes(self):
        response = c.delete(f"/api/v1/users/{self.u.id}/projects/{self.p.id}/")
        self.assertEqual(response.status_code, 200)

    def test_project_doesnt_delete(self):
        response = c.delete(f"/api/v1/users/{self.u.id}/projects/-1/")
        self.assertEqual(response.status_code, 404)