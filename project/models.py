from django.db import models
from user.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    steps = models.TextField(max_length=2000)
    description = models.TextField(max_length=2000)
    features = models.TextField(max_length=2000)
    interactions = models.TextField(max_length=2000)
    colors = models.TextField(max_length=2000)
    timeline = models.CharField(max_length=6)
    saved = models.BooleanField(default=False)
    tagline = models.TextField(max_length=2000)
    collaborators = models.PositiveSmallIntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def serialize_project(serializer, project_id):
        return {
                    "data":
                    {
                        "id": f"{project_id}",
                        "type": "project",
                        "attributes": serializer.data,
                    }
                }