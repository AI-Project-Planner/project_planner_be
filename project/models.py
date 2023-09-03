from django.db import models
from user.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    steps = models.TextField(max_length=2000)
    description = models.TextField(max_length=2000)
    features = models.TextField(max_length=2000)
    interactions = models.TextField(max_length=2000)
    technologies = models.TextField(max_length=2000)
    colors = models.TextField(max_length=2000)
    timeline = models.CharField(max_length=6)
    timeline_int = models.PositiveSmallIntegerField(default=0)
    saved = models.BooleanField(default=False)
    tagline = models.TextField(max_length=2000)
    collaborators = models.PositiveSmallIntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    logo_url = models.TextField(max_length=2000, blank=True)
    logo_font = models.TextField(max_length=2000, blank=True)

    def serialize_project(serializer, project_id):
        return {
                    "data":
                    {
                        "id": f"{project_id}",
                        "type": "project",
                        "attributes": serializer.data,
                    }
                }

    def serialize_all_projects(projects):
        array = []
        for x in projects:
            z = {
                "id": f"{x.id}",
                "type": "project",
                "attributes":
                    {
                        "name": f"{x.name}",
                        "steps": f"{x.steps}",
                        "description": f"{x.description}",
                        "features": f"{x.features}",
                        "interactions": f"{x.interactions}",
                        "technologies": f"{x.technologies}",
                        "colors": f"{x.colors}",
                        "timeline": f"{x.timeline}",
                        "timeline_int": x.timeline_int,
                        "saved": x.saved,
                        "tagline": f"{x.tagline}",
                        "collaborators": x.collaborators,
                        "user_id": x.user_id.id,
                        "logo_url": x.logo_url,
                        "logo_font": x.logo_font
                    }
            }
            array.append(z)
        return { "data": array }