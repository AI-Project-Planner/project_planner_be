from django.test import TestCase, Client
from .models import Project
from user.models import User
from importlib import reload
import code

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
        self.assertEqual(self.p.logo_url, "")
        self.assertEqual(self.p.logo_font, "")

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
        self.assertContains(response, 'logo_url')
        self.assertContains(response, 'logo_font')

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

    def test_project_all_fields_updated(self):
        payload = {
            "name": "UPDATED: TaskMaster Pro",
            "steps": "UPDATED: Project Setup: Create Git repository and define project structure\nBackend Setup: Develop Express.js application, set up API routes\nDatabase Design: Design and implement database schema",
            "description": "UPDATED: TaskMaster Pro is an all-inclusive task management application designed to optimize team collaboration and productivity.",
            "features": "UPDATED: User registration and login\nCreate, assign, update, and track tasks\nReal-time collaboration and updates\nPriority-based task categorization",
            "interactions": "UPDATED: User logs in to TaskMaster Pro account.\nDashboard displays tasks by priority: High, Medium, Low.\nUser adds a task, assigns it, and sets a due date.\nTask appears under the respective priority category.\nAssigned user starts task, status updates in real-time.\nUpon completion, task is marked as done and updates for all.",
            "colors": "UPDATED: #3498DB\n#27AE60\n#F39C12\n#F0F3F4\n#333333\n#E74C3C",
            "technologies": "UPDATED: react, typescript and javascript",
            "timeline": "UPDATE",
            "timeline_int": 10,
            "tagline": "UPDATED: Stay organized and track progress",
            "collaborators": 10,
            "saved": "true",
            "user_id": 1,
            "logo_url": "",
            "logo_font": "",
        }

        response = c.put(f"/api/v1/users/{self.u.id}/projects/{self.p.id}/", data=payload, content_type='application/json')
        self.assertEqual(response.status_code, 202)
        self.p.refresh_from_db()
        self.assertEqual(self.p.user_id, self.u)
        self.assertEqual(self.p.name, self.p.name)
        self.assertEqual(self.p.description, payload['description'])
        self.assertEqual(self.p.steps, payload['steps'])
        self.assertEqual(self.p.colors, payload['colors'])
        self.assertEqual(self.p.features, payload['features'])
        self.assertEqual(self.p.technologies, payload['technologies'])
        self.assertEqual(self.p.interactions, payload['interactions'])
        self.assertEqual(self.p.timeline, payload['timeline'])
        self.assertEqual(self.p.timeline_int, payload['timeline_int'])
        self.assertEqual(self.p.tagline, payload['tagline'])
        self.assertEqual(self.p.collaborators, payload['collaborators'])
        self.assertEqual(self.p.saved, True)
        self.assertEqual(self.p.logo_url, payload['logo_url'])
        self.assertEqual(self.p.logo_font, payload['logo_font'])

    def test_get_all_users_projects(self):
        response = c.get(f"/api/v1/users/{self.u.id}/projects/")
        self.assertEqual(response.status_code, 200)

    def test_get_all_users_projects_user_not_found(self):
        response = c.get("/api/v1/users/-1/projects/")
        self.assertEqual(response.status_code, 404)

    def test_project_deletes(self):
        self.assertEqual(Project.objects.count(), 2)
        response = c.delete(f"/api/v1/users/{self.u.id}/projects/{self.p.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Project.objects.count(), 1)

    def test_project_doesnt_delete(self):
        response = c.delete(f"/api/v1/users/{self.u.id}/projects/-1/")
        self.assertEqual(response.status_code, 404)