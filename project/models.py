from django.db import models
from user.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=1000)
    steps = models.TextField(max_length=1000)
    features = models.TextField(max_length=1000)
    colors = models.TextField(max_length=1000)
    interactions = models.TextField(max_length=1000)
    timeline = models.TextField(max_length=254)
    saved = models.BooleanField(default=False)


    def serialize_project(serializer, id):
        return {
                  "data": {
                      "id": f"{id}",
                      "type": "project",
                      "attributes": serializer.data,
                  }
                }